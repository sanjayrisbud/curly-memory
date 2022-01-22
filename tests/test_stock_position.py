""" Tests for StockPosition class. """
from datetime import datetime
from models.stock_position import StockPosition


def test_init():
    """Unit test for initializer."""
    record = StockPosition(datetime.today(), "abc", "100", "25", "75.8")
    assert record.stock == "abc"
    assert record.shares == 100
    assert record.total_cost == 75.8


def test_compute_pct_profit_or_loss():
    """Unit test for compute_pct_profit_or_loss()"""
    record = StockPosition(datetime.today(), "abc", "100", "25", "0")
    pct = record.compute_pct_profit_or_loss()
    assert pct == 0


def test_get_status():
    """Unit test for get_status()."""
    record = StockPosition(datetime.today(), "abc", "100", "25", "75.8")
    assert record.get_status() == "loss"
    record = StockPosition(datetime.today(), "abc", "100", "25", "25")
    assert record.get_status() == "break even"
    record = StockPosition(datetime.today(), "abc", "100", "225", "75.8")
    assert record.get_status() == "gain"
    record = StockPosition(datetime.today(), "abc", "100", "225", "0")
    assert record.get_status() == "unknown"


def test_str():
    """Unit test for __str__()"""
    record = StockPosition(datetime.today(), "abc", "100", "25", "0")
    assert str(record) == "abc-->25.0"
