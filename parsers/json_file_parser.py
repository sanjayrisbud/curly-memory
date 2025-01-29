"""Defines the JsonFileParser class."""
from extractors.json_extractor import JsonExtractor
from parsers.parser import Parser


class JsonFileParser(Parser):
    """Parser for the JSON containing additional data."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = JsonExtractor(filename, self.path, self.date)

    def parse(self):
        """Nothing for now."""
