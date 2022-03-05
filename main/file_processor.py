"""Defines FileProcessor class."""
import shutil
from datetime import datetime
from pathlib import Path


class FileProcessor:
    """Class to manipulate files."""

    def __init__(self, filename, path, date, archive_path=None):
        self.path = Path(path)
        self.file_object = self.path / filename
        self.date = date or datetime.today()
        self.archive_path = (
            Path(archive_path) if archive_path else self.path / "archive"
        )

    def file_exists(self):
        """Return True if file exists, False otherwise."""
        return self.file_object.exists()

    def archive(self):
        """Move the file to the archive folder, appending current date."""
        old_name = str(self.path / self.file_object.stem)
        suffix = self.file_object.suffix
        new_name = str(self.archive_path / self.file_object.stem) + self.date.strftime(
            "_%Y-%m-%d"
        )
        return shutil.copy(old_name + suffix, new_name + suffix)
