"""Defines the ReportsCreator class."""
from openpyxl import load_workbook
from charts.summary_chart import SummaryChart


class ReportsCreator:
    """Class used to create the financial reports."""

    def __init__(self, statement, db_interface=None):
        self._statement = statement
        self._financial_data = None
        self._db_interface = db_interface
        self._charts_to_create = [
            ("SALN Chart", SummaryChart)
        ]

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
        self.financial_data = data
        file_object = self._statement.file_object
        workbook = load_workbook(file_object)
        for chart in self._charts_to_create:
            sheet = workbook.create_sheet(title=chart[0])
            image = chart[1](data).get_image()
            image.anchor = "A1"
            sheet.add_image(image)
        workbook.save(file_object)
