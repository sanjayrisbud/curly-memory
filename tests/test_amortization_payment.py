""" Tests for AmortizationPayment class. """
from datetime import datetime
from models.amortization_payment import AmortizationPayment


def test_init():
    """Unit test for initializer."""
    record = AmortizationPayment("1", "Jan 1 1900", "100", "25", "75", "400")
    assert record.payment_number == 1
    assert record.balance == 400


def test_convert_date_to_datetime():
    """Unit test for convert_date_to_datetime()"""
    date = "Jan 1 1900"
    returned_date = AmortizationPayment.convert_date_to_datetime(date)
    assert returned_date == datetime(1900, 1, 1)


def test_is_valid():
    """Unit test for is_valid()."""
    valid = AmortizationPayment("1", "Jan 1 1900", "100", "25", "75", "400")
    invalid = AmortizationPayment("1", "Jan 1 1900", "100", "2", "75", "400")
    assert valid.is_valid()
    assert not invalid.is_valid()
