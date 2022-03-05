"""Defines the Parser class."""
import logging


class Parser:
    """Parent class of all parsers."""

    def __init__(self, path, date):
        self.path = path
        self.date = date
        self.extractor = None
        self.parsed_data = []
        self.total_amount = 0

    def get_data(self):
        """Extract and parse the data from the file."""
        if self.extractor:
            if self.extractor.is_stale():
                logging.warning(
                    "%s is stale, consider re-downloading.", self.extractor.file_object
                )
            self.extractor.extract()
        self.parse()

    def parse(self):
        """Parse the file content."""
        raise NotImplementedError()

    def append(self, model):
        """Append the new record to the internal list."""
        self.parsed_data.append(model)
