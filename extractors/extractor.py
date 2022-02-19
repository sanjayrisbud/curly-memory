""" Defines Extractor class. """
from datetime import datetime, timedelta

from main.file_processor import FileProcessor


class Extractor(FileProcessor):
    """Parent class of all extractors."""

    def __init__(self, filename, path=None, date=None):
        super().__init__(filename, path, date)
        self.raw_data = None
        self.file_type = ""

    def is_stale(self):
        """Determine whether associated file is already stale."""
        modified = datetime.fromtimestamp(self.file_object.stat().st_mtime)
        return self.date - modified > timedelta(days=15)

    def extract(self):
        """Extract data from file."""
        raise NotImplementedError()
