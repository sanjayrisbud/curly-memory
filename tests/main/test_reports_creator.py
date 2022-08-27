"""Tests for the ReportsCreator class."""
from datetime import datetime
import models
from main.db_interface import DatabaseInterface
from main.file_processor import FileProcessor
from main.reports_creator import ReportsCreator


def test_run(writable_path):
    """Unit test for run()."""
    statement = FileProcessor("dummy.xlsx", writable_path, datetime(2000, 1, 1))
    db_file = FileProcessor("db.sqlite3", path=writable_path, date=None)
    db_engine = models.get_engine(writable_path + "/db.sqlite3")
    creator = ReportsCreator(
        statement=statement, db_interface=DatabaseInterface(db_file, db_engine)
    )
    creator.run(([], {}, {}))
    assert creator.statement.file_object.exists()
    creator.statement.file_object.unlink()


def test_get_previous_financial_data(writable_path):
    """Unit test for get_previous_financial_data()."""
    creator = ReportsCreator(
        FileProcessor("dummy.xlsx", writable_path, datetime(2000, 1, 1))
    )
    assert creator.get_previous_financial_data()[0] == []
