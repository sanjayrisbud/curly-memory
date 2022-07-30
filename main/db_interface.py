"""Defines the DatabaseInterface class."""
from models import summary


class DatabaseInterface:
    """Class used to interface with the database."""

    def __init__(self, db_file, db_engine):
        self._db_file = db_file
        self._db_engine = db_engine

    def archive_db_file(self):
        """Archive the database file."""
        self._db_file.archive()

    def get_previous_financial_data(self):
        """Get previous financial data."""
        previous = summary.Summary.get_date_right_before(
            self._db_engine, date=self._db_file.date
        )[0][0]
        records = list(summary.Summary.find_by_date(self._db_engine, date=previous))
        return records, {}, {}

    def store_various_financial_data(self, financial_data):
        """Store various financial data points in the database for later use."""
        for summ in financial_data[0]:
            summ.insert(self._db_engine)
        for bank_account in financial_data[1]["BankAccounts"]["records"]:
            bank_account.insert(self._db_engine)
        for stock in financial_data[1]["Portfolio"]["records"]:
            stock.insert(self._db_engine)

    def get_time_series_summary(self):
        """Return a summary of asset and liability values as 3 time series."""
        result = summary.Summary.get_asset_and_liability_values(self._db_engine)
        date_points = [row[0] for row in result[0]]
        asset_points = [row[2] for row in result[0]]
        liability_points = [row[2] for row in result[1]]
        return date_points, asset_points, liability_points
