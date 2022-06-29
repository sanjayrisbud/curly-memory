"""Tests for the StatementWriter class."""
from datetime import datetime

from openpyxl import Workbook

from main.file_processor import FileProcessor
from main.statement_writer import StatementWriter


def test_run(writable_path):
    """Unit test for run()."""
    writer = StatementWriter(
        FileProcessor("dummy.xlsx", writable_path, datetime(2000, 1, 1)))
    writer.run(([], {}, {}))
    assert writer.statement.file_object.exists()
    writer.statement.file_object.unlink()


def test_populate_summary_sheet(writable_path):
    """Unit test for populate_summary_sheet()."""
    stmt = StatementWriter(
        FileProcessor("dummy.xlsx", writable_path, datetime(2000, 1, 1))
    )
    workbook = Workbook()
    worksheet = workbook.create_sheet()
    stmt.financial_data = [], {}, {}
    stmt.populate_summary_sheet(worksheet)
    assert worksheet["A3"].value == "January 2000"
    workbook.close()
