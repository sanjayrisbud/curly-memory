"""Defines BankAccount class."""


class BankAccount:
    """Model for a bank account/insurance policy."""

    def __init__(self, *args):
        date, bank, account_alias, account_number, balance = args
        self.date = date
        self.bank = bank
        self.account_alias = account_alias
        self.account_number = account_number
        self.balance = float(balance)

    def is_asset(self):
        """Check whether the bank account is an asset."""
        return self.account_alias != "MasterCard"

    def __str__(self):
        """String equivalent of object."""
        return f"{self.account_alias} ({self.bank} {self.account_number}) --> {self.balance}"
