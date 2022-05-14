"""Defines the ReportsCreator class."""


class ReportsCreator:
    """Class used to create the financial reports."""

    def __init__(self, statement, db_engine):
        self.statement = statement
        self.db_engine = db_engine

    def run(self):
        """Perform class logic."""
