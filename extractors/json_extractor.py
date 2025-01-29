"""Defines the JsonExtractor class."""

import json

from extractors.extractor import Extractor


class JsonExtractor(Extractor):
    """Class for extracting data from JSONs."""

    def __init__(self, filename, path=None, date=None):
        super().__init__(filename, path, date)
        self.file_type = "json"

    def extract(self):
        """Return a dict representing the contents of the file."""
        with open(self.file_object, mode="r", encoding="utf-8") as file:
            self.raw_data = json.load(file)
