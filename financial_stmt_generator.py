"""Defines the FinancialStatementGenerator class."""
from datetime import datetime
from parsers.amortization_schedule_parser import AmortizationScheduleParser
from parsers.mutual_funds_parser import MutualFundsParser
from parsers.portfolio_parser import PortfolioParser
from parsers.bank_accounts_parser import BankAccountsParser
from parsers.insurance_policies_parser import InsurancePoliciesParser
from parsers.real_estate_parser import RealEstateParser
from main.statement_writer import StatementWriter


class FinancialStatementGenerator:
    """Class to generate financial statement."""

    def __init__(self):
        path = "C:/Users/sanjay s risbud/Dropbox/statements"
        date = datetime.today()

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

        self.statement_writer = StatementWriter("financial_statement.xlsx", path, date)

    def run(self):
        """Run the application logic."""
        self.mine_data()
        self.write_statement()

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
    generator = FinancialStatementGenerator()
    generator.run()


if __name__ == "__main__":
    main()
