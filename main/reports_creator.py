"""Defines the ReportsCreator class."""
from openpyxl import load_workbook


class ReportsCreator:
    """Class used to create the financial reports."""

    def __init__(self, statement, db_interface=None):
        self._statement = statement
        self._financial_data = None
        self._db_interface = db_interface

    @property
    def statement(self):
        """Return the financial statement."""
        return self._statement

    @property
    def financial_data(self):
        """Return the financial data."""
        if not self._financial_data:
            self.financial_data = self.get_previous_financial_data()
        return self._financial_data

    @financial_data.setter
    def financial_data(self, financial_data):
        """Set the financial data."""
        self._financial_data = financial_data

    def get_previous_financial_data(self):
        """Get the previous financial data."""
        if not self._db_interface:
            return [], {}, {}
        return self._db_interface.get_previous_financial_data()

    def run(self, data):
        """Perform class logic."""
        self._financial_data = data
        file_object = self._statement.file_object
        workbook = load_workbook(file_object)
        workbook.save(file_object)
