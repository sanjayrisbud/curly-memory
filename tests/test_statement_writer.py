"""Tests for the StatementWriter class."""
from datetime import datetime
from pathlib import Path

from openpyxl import Workbook

from misc.statement_writer import StatementWriter


def test_run():
    """Unit test for run()."""
    stmt = StatementWriter("dummy", None, datetime(2000, 1, 1))
    archived_file = Path(stmt.run({}))
    assert stmt.file_object.exists()
    assert archived_file.exists()
    stmt.file_object.unlink()
    archived_file.unlink()


def test_populate_summary_sheet():
    """Unit test for populate_summary_sheet()."""
    stmt = StatementWriter("dummy", None, datetime(2000, 1, 1))
    workbook = Workbook()
    worksheet = workbook.create_sheet()
    stmt.data = {}
    stmt.populate_summary_sheet(worksheet)
    assert worksheet["A3"].value == "January 2000"
