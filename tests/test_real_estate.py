"""Test RealEstate class."""
from datetime import datetime
from models.real_estate import RealEstate


def test_init():
    """Unit test for __init__()."""
    record = RealEstate(datetime.today(), "a", 2010, 100000, 10)
    assert record.market_value == 100000


def test_compute_market_value():
    """Unit test for compute_market_value()."""
    record = RealEstate(datetime.today(), "a", 2010, 100000, 10)
    record.compute_market_value(5)
    assert record.market_value == 50000


def test_str():
    """Unit test for __str__()."""
    record = RealEstate(datetime.today(), "a", 2010, 100000, 10)
    assert str(record) == "a (acquired 2010) --> 100000"
