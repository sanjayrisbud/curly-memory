"""Test Summary class."""
from datetime import datetime
from models.summary import Summary


def test_insert():
    """Unit test for insert()."""
    record = Summary(datetime.today(), "a", 23)
    record_id = record.insert()
    assert record_id > 0


def test_insert_many():
    """Unit test for insert_many()."""
    records = [Summary(datetime.today(), "a", 23), Summary(datetime.today(), "b", 24)]
    record_ids = Summary.insert_many(records)
    assert len(record_ids) > 0 and all(record_ids)


def test_find_by_date():
    """Unit test for find_by_date()."""
    date = datetime.today()
    records = [
        Summary(date, "c", 1.5),
        Summary(datetime(2019, 6, 3), "x", -1),
        Summary(date, "d", 2.4),
    ]
    Summary.insert_many(records)
    found = Summary.find_by_date(date)
    assert len([1 for row in found]) == 2


def test_str():
    """Unit test for str()."""
    record = Summary(datetime(2019, 6, 3), "x", -1)
    assert str(record) == "x-->-1"
