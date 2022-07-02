"""Defines the DatabaseInterface class."""


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
        print(self)
        return [], {}, {}

    def store_various_financial_data(self, financial_data):
        """Store various financial data points in the database for later use."""
        for summary in financial_data[0]:
            summary.insert(self._db_engine)
        for bank_account in financial_data[1]["BankAccounts"]["records"]:
            bank_account.insert(self._db_engine)
        for stock in financial_data[1]["Portfolio"]["records"]:
            stock.insert(self._db_engine)
