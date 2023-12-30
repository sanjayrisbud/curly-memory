"""Defines BankAccountsParser class."""
import re

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
        offset += 1
        deposits = int(self.lines[offset])
        for i in range(0, deposits):
            self.create_entry(
                "BPI",
                account_alias=self.lines[4 * i + offset + 1],
                account_number=re.search(r"\d+", self.lines[4 * i + offset + 2])[0],
                balance=re.search(r"[\d,\.]+", self.lines[4 * i + offset + 3])[0],
            )

        # get the credit card
        offset = self.return_line_that_starts_with("Credit cards")
        if offset > -1:
            self.create_entry(
                "BPI",
                account_alias=self.lines[offset + 2],
                account_number=re.search(r"\d+", self.lines[offset + 4])[0],
                balance=re.search(r"[\d,\.]+", self.lines[offset + 5])[0],
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
