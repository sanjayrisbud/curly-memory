"""Defines the FinancialStatementGenerator class."""
import argparse
from datetime import datetime

import models
from main.file_processor import FileProcessor
from main.reports_creator import ReportsCreator
from main.statement_writer import StatementWriter
from parsers.amortization_schedule_parser import AmortizationScheduleParser
from parsers.bank_accounts_parser import BankAccountsParser
from parsers.insurance_policies_parser import InsurancePoliciesParser
from parsers.mutual_funds_parser import MutualFundsParser
from parsers.portfolio_parser import PortfolioParser
from parsers.real_estate_parser import RealEstateParser


class FinancialStatementGenerator:
    """Class to generate financial statement."""

    def __init__(self, environment):
        path = "C:/Users/sanjay s risbud/Dropbox/statements"
        path_for_writes = path if environment == "prod" else path + "/tests"
        date = datetime.today()

        self.statement = FileProcessor(
            "financial_statement.xlsx", path_for_writes, date
        )
        self.db_file = FileProcessor(
            "db.sqlite3",
            path=path_for_writes,
            date=date,
            archive_path=self.statement.archive_path,
        )
        self.db_engine = models.get_engine(path_for_writes + "/db.sqlite3")

        self.asset_parsers = [
            BankAccountsParser("BPI Online.pdf", path, date),
            PortfolioParser("BPI Trade - Stock Position.html", path, date),
            InsurancePoliciesParser(
                "Sun Life Financial - Philippines.html", path, date
            ),
            MutualFundsParser("Sun Life Financial - Philippines.html", path, date),
            RealEstateParser(path, date),
        ]

        self.liability_parsers = [
            AmortizationScheduleParser("loan.html", path, date),
        ]

        self.statement_writer = StatementWriter(self.statement, self.db_engine)
        self.reports_creator = ReportsCreator(self.statement, self.db_engine)

    def run(self, environment):
        """Run the application logic."""
        self.mine_data()
        if environment != "dev":
            self.write_statement()
        else:
            self.reports_creator.run()
        self.statement.archive()
        self.db_file.archive()

    def mine_data(self):
        """Mine the data to be used to populate the statement."""
        for parser in self.asset_parsers:
            parser.get_data()
            if parser.extractor:
                parser.extractor.archive()

        for parser in self.liability_parsers:
            parser.get_data()

    def write_statement(self):
        """Write out the financial statement, sourcing the mined data."""
        credit_card_list = [
            account
            for account in self.asset_parsers[0].parsed_data
            if not account.is_asset()
        ]
        credit_card = credit_card_list[0] if len(credit_card_list) == 1 else None
        data = vars(self)
        data["credit_card"] = credit_card
        self.statement_writer.run(data)


def main():
    """Program entrypoint."""
    parser = argparse.ArgumentParser()
    parser.add_argument("environment", help="Environment in which to run the program.")
    args = parser.parse_args()
    generator = FinancialStatementGenerator(args.environment)
    generator.run(args.environment)


if __name__ == "__main__":
    main()
