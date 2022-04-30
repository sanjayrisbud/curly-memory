"""Defines BankAccountsParser class."""
from extractors.pdf_extractor import PDFExtractor
from models.bank_account import BankAccount
from parsers.parser import Parser


class BankAccountsParser(Parser):
    """Parser for the bank accounts."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = PDFExtractor(filename, self.path, self.date)

    def parse(self):
        """Parse the account information."""
        lines = self.extractor.raw_data[0].split("\n")

        # determine the number of deposit accounts
        deposits = int(lines[2].split("(")[1][0])
        for i in range(1, deposits + 1):
            self.create_entry(
                "BPI", lines[4 * i + 0], lines[4 * i + 1], lines[4 * i + 2]
            )

        # get the credit card
        if len(lines) > 30:
            self.create_entry("BPI", lines[30], lines[31], lines[32])

        # MANUAL ENTRY FOR CIMB ACCT
        self.create_entry("CIMB Bank", "GSave", "20860739494592", "500,000")

    def create_entry(self, bank, account_alias, account_number, balance):
        """Add to list of bank accounts and to total_amount (if necessary)."""
        account_alias = account_alias.strip()
        account_number = account_number.strip()
        balance = balance.strip().replace(",", "")
        record = BankAccount(self.date, bank, account_alias, account_number, balance)
        self.parsed_data.append(record)
        if record.is_asset():
            self.total_amount += record.balance
