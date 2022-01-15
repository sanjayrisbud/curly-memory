"""Defines AmortizationPayment class."""


from datetime import datetime


class AmortizationPayment:
    """Model for an AmortizationPayment."""

    def __init__(self, *args):
        payment_number, date, amount, principal, interest, balance = args
        self.payment_number = int(payment_number)
        self.date = self.convert_date_to_datetime(date)
        self.amount = float(amount)
        self.principal = float(principal)
        self.interest = float(interest)
        self.balance = float(balance)

    @staticmethod
    def convert_date_to_datetime(date):
        """Convert the input string to datetime."""
        return datetime.strptime(date, "%b %d %Y")

    def is_valid(self):
        """Check whether principal + interest is equal to amount."""
        return self.principal + self.interest == self.amount
