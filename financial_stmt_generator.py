"""Defines the FinancialStatementGenerator class."""
import argparse
from datetime import datetime

import models
from main.db_interface import DatabaseInterface
from main.file_processor import FileProcessor
from main.reports_creator import ReportsCreator
from main.statement_writer import StatementWriter
from models.bank_account import BankAccount
from models.summary import Summary
from parsers.amortization_schedule_parser import AmortizationScheduleParser
from parsers.bank_accounts_parser import BankAccountsParser
from parsers.insurance_policies_parser import InsurancePoliciesParser
from parsers.mutual_funds_parser import MutualFundsParser
from parsers.portfolio_parser import PortfolioParser
from parsers.real_estate_parser import RealEstateParser


class FinancialStatementGenerator:
    """Class to generate financial _statement."""

    def __init__(self, environment):
        path = "C:/Users/sanjay s risbud/Dropbox/statements"
        path_for_writes = path if environment == "prod" else path + "/tests"
        date = datetime.today()

        self.statement = FileProcessor(
            "financial_statement.xlsx", path_for_writes, date
        )
        db_file = FileProcessor(
            "db.sqlite3",
            path=path_for_writes,
            date=date,
            archive_path=self.statement.archive_path,
        )
        db_engine = models.get_engine(path_for_writes + "/db.sqlite3")

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

        self.db_interface = DatabaseInterface(db_file, db_engine)
        self.statement_writer = StatementWriter(self.statement)
        self.reports_creator = ReportsCreator(self.statement, self.db_interface)

    def run(self, environment):
        """Run the application logic."""
        data = self.mine_data()
        if environment != "dev":
            self.statement_writer.run(data)
        else:
            self.reports_creator.run(data)
        self.statement.archive()
        self.db_interface.archive_db_file()

    def mine_data(self):
        """Mine the _financial_data to be used to populate the _statement."""
        for parser in self.asset_parsers:
            parser.get_data()
            if parser.extractor:
                parser.extractor.archive()

        for parser in self.liability_parsers:
            parser.get_data()

        return self.consolidate_financial_data()

    def consolidate_financial_data(self):
        """Consolidate the _financial_data from the asset and liability parsers."""
        assets = {}
        for parser in self.asset_parsers:
            assets[parser.__class__.__name__.replace("Parser", "")] = {
                "records": parser.parsed_data,
                "total_amount": parser.total_amount
            }
        liabilities = {}
        for parser in self.liability_parsers:
            liabilities[parser.__class__.__name__.replace("Parser", "")] = {
                "records": parser.parsed_data,
                "total_amount": parser.total_amount
            }
        self.move_credit_cards_to_liabilities(assets, liabilities)
        summary = self.generate_summary_entries(assets, liabilities, self.statement.date)
        return summary, assets, liabilities

    @staticmethod
    def move_credit_cards_to_liabilities(assets, liabilities):
        """Move the credit cards (if any) from to liabilities."""
        credit_cards = []
        to_delete = []
        total_amount = 0
        for account in assets.get("BankAccounts", {}).get("records", {}):
            if not account.is_asset():
                total_amount += account.balance
                card = BankAccount(account.date, account.bank, account.account_alias,
                                   account.account_number, account.balance)
                to_delete.append(account)
                credit_cards.append(card)

        for account in to_delete:
            assets["BankAccounts"]["records"].remove(account)
        liabilities["CreditCard"] = {"records": credit_cards, "total_amount": total_amount}

    @staticmethod
    def generate_summary_entries(assets, liabilities, date):
        """Generate a summary of asset and liability entries."""
        summary = []
        for type_, asset in assets.items():
            summary.append(Summary(date, "ASSET", type_, asset["total_amount"]))
        for type_, liability in liabilities.items():
            summary.append(Summary(date, "LIABILITY", type_, liability["total_amount"]))
        return summary


def main():
    """Program entrypoint."""
    parser = argparse.ArgumentParser()
    parser.add_argument("environment", help="Environment in which to run the program.")
    args = parser.parse_args()
    generator = FinancialStatementGenerator(args.environment)
    generator.run(args.environment)


if __name__ == "__main__":
    main()
