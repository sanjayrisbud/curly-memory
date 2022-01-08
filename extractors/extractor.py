""" Defines Extractor class. """
import shutil
from datetime import datetime
from pathlib import Path


class Extractor:
    """Parent class of all extractors."""

    PATH = Path("C:/Users/sanjay s risbud/Dropbox/statements")

    def __init__(self, filename, date=None):
        self.file_object = self.PATH / filename
        self.file_type = ""
        if isinstance(date, datetime):
            self.date = date
        else:
            self.date = datetime.today()

    def file_exists(self):
        """Return True if file exists, False otherwise."""
        return self.file_object.exists()

    def archive(self):
        """Move the file to the archive folder, appending current date."""
        old_name = str(self.PATH / self.file_object.name)
        suffix = self.file_object.suffix
        new_name = str(
            self.PATH / "archive" / self.file_object.name
        ) + self.date.strftime("_%Y-%m-%d")
        return shutil.move(old_name + suffix, new_name + suffix)
