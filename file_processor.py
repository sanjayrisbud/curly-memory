"""Defines FileProcessor class."""
import shutil
from datetime import datetime
from pathlib import Path


class FileProcessor:
    """Parent class of classes that manipulate files."""

    def __init__(self, filename, path, date):
        folder = path or "C:/Users/sanjay s risbud/Dropbox/statements"
        self.path = Path(folder)
        self.file_object = self.path / filename
        self.date = date or datetime.today()

    def file_exists(self):
        """Return True if file exists, False otherwise."""
        return self.file_object.exists()

    def archive(self):
        """Move the file to the archive folder, appending current date."""
        old_name = str(self.path / self.file_object.stem)
        suffix = self.file_object.suffix
        new_name = str(
            self.path / "archive" / self.file_object.stem
        ) + self.date.strftime("_%Y-%m-%d")
        return shutil.copy(old_name + suffix, new_name + suffix)
