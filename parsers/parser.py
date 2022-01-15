"""Defines the Parser class."""
from datetime import datetime


class Parser:
    """Parent class of all parsers."""

    def __init__(self, path=None, date=None):
        self.path = path or "C:/Users/sanjay s risbud/Dropbox/statements"
        self.date = date or datetime.today()
        self.extractor = None
        self.parsed_data = []

    def parse(self):
        """Parse the file content."""
        raise NotImplementedError()

    def append(self, model):
        """Append the new record to the internal list."""
        self.parsed_data.append(model)
