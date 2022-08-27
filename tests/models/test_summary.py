"""Test Summary class."""
from datetime import datetime
from models.summary import Summary


def test_insert(engine):
    """Unit test for insert()."""
    date = datetime(2019, 5, 3)
    record = Summary(date, "ASSET", "a", 23)
    record_id = record.insert(engine)
    assert record_id > 0
    record = Summary(date, "LIABILITY", "b", 24)
    record_id = record.insert(engine)
    assert record_id > 0


def test_insert_many(engine):
    """Unit test for insert_many()."""
    date = datetime(2019, 6, 3)
    records = [
        Summary(date, "ASSET", "a", 23),
        Summary(date, "LIABILITY", "b", 24),
    ]
    record_ids = Summary.insert_many(engine, records)
    assert len(record_ids) % 2 == 0 and all(record_ids)


def test_find_by_date(engine):
    """Unit test for find_by_date()."""
    date = datetime(2019, 7, 3)
    records = [
        Summary(date, "LIABILITY", "c", 1.5),
        Summary(date, "ASSET", "x", -1),
        Summary(date, "LIABILITY", "d", 2.4),
    ]
    Summary.insert_many(engine, records)
    found = Summary.find_by_date(engine, date)
    assert len([1 for _ in found]) % 3 == 0


def test_str():
    """Unit test for str()."""
    record = Summary(datetime(2019, 6, 3), "ASSET", "x", -1)
    assert str(record) == "x-->-1"
