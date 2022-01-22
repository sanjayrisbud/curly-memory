""" Defines Extractor class. """
import shutil
from datetime import datetime, timedelta
from pathlib import Path


class Extractor:
    """Parent class of all extractors."""

    def __init__(self, filename, path=None, date=None):
        folder = path or "C:/Users/sanjay s risbud/Dropbox/statements"
        self.path = Path(folder)
        self.file_object = self.path / filename
        self.file_type = ""
        self.raw_data = None
        self.date = date or datetime.today()

    def file_exists(self):
        """Return True if file exists, False otherwise."""
        return self.file_object.exists()

    def archive(self):
        """Move the file to the archive folder, appending current date."""
        old_name = str(self.path / self.file_object.name)
        suffix = self.file_object.suffix
        new_name = str(
            self.path / "archive" / self.file_object.name
        ) + self.date.strftime("_%Y-%m-%d")
        return shutil.copy(old_name + suffix, new_name + suffix)

    def is_stale(self):
        """Determine whether associated file is already stale."""
        modified = datetime.fromtimestamp(self.file_object.stat().st_mtime)
        return self.date - modified > timedelta(days=15)

    def extract(self):
        """Extract data from file."""
        raise NotImplementedError()
