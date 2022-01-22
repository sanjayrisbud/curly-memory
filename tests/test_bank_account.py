"""Test BankAccount class."""
from datetime import datetime
from models.bank_account import BankAccount


def test_init():
    """Unit test for __init__()."""
    record = BankAccount(datetime.today(), "a", "b", "c", 23)
    assert record.balance == 23


def test_is_asset():
    """Unit test for is_asset()."""
    record = BankAccount(datetime.today(), "a", "b", "c", 23)
    assert record.is_asset()


def test_str():
    """Unit test for __str__()."""
    record = BankAccount(datetime.today(), "a", "b", "c", 23)
    assert str(record) == "b (a c) --> 23.0"
