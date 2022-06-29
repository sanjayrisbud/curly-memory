"""Tests for the ReportsCreator class."""
from datetime import datetime
from main.file_processor import FileProcessor
from main.reports_creator import ReportsCreator


def test_run(writable_path):
    """Unit test for run()."""
    creator = ReportsCreator(
        FileProcessor("dummy.xlsx", writable_path, datetime(2000, 1, 1))
    )
    creator.run(([], {}, {}))
    assert creator.statement.file_object.exists()
    creator.statement.file_object.unlink()
