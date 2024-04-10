"""Defines the CsvExtractor class."""

import csv

from extractors.extractor import Extractor


class CsvExtractor(Extractor):
    """Class for extracting data from CSVs."""

    def __init__(self, filename, path=None, date=None):
        super().__init__(filename, path, date)
        self.file_type = "csv"

    def extract(self):
        """Return a list of lists representing the contents of the file."""
        with open(self.file_object, mode="r", encoding="utf-8") as file:
            self.raw_data = list(csv.reader(file))
