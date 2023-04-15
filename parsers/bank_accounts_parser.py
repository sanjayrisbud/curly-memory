"""Defines BankAccountsParser class."""
from extractors.pdf_extractor import PDFExtractor
from models.bank_account import BankAccount
from parsers.parser import Parser


class BankAccountsParser(Parser):
    """Parser for the bank accounts."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = PDFExtractor(filename, self.path, self.date)
        self.lines = None

    def parse(self):
        """Parse the account information."""
        self.lines = self.extractor.raw_data[0].split("\n")

        # determine the number of deposit accounts
        offset = self.return_line_that_starts_with("Deposit")
        deposits = int(self.lines[offset].split("(")[1][0])
        for i in range(1, deposits + 1):
            self.create_entry(
                "BPI",
                self.lines[4 * i + offset - 2],
                self.lines[4 * i + offset - 1],
                self.lines[4 * i + offset],
            )

        # get the credit card
        offset = self.return_line_that_starts_with("Credit Card")
        if offset > -1:
            self.create_entry(
                "BPI",
                self.lines[offset + 2],
                self.lines[offset + 3],
                self.lines[offset + 4],
            )

        # MANUAL ENTRY FOR CIMB ACCT
        self.create_entry("CIMB Bank", "GSave", "20860739494592", "293,000")

    def create_entry(self, bank, account_alias, account_number, balance):
        """Add to list of bank accounts and to total_amount (if necessary)."""
        account_alias = account_alias.strip()
        account_number = account_number.strip()
        balance = balance.strip().replace(",", "")
        record = BankAccount(self.date, bank, account_alias, account_number, balance)
        self.parsed_data.append(record)
        if record.is_asset():
            self.total_amount += record.balance

    def return_line_that_starts_with(self, prefix):
        """Return the index of the first line that starts with the given prefix."""
        for i, line in enumerate(self.lines):
            if line.startswith(prefix):
                return i
        return -1
