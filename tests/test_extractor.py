""" Unit tests for Extractor class. """
import tempfile
from datetime import datetime
from pathlib import Path
from extractors.extractor import Extractor


def test_init():
    """Unit test for initializer."""
    extractor = Extractor("dummy_file")
    assert isinstance(extractor.file_object, Path)
    assert extractor.date == datetime.today()
    assert extractor.file_type == ""
    dummy_date = datetime(2022, 1, 1)
    extractor = Extractor("dummy_file", dummy_date)
    assert extractor.date == dummy_date


def test_file_exists():
    """Unit test for file_exists()."""
    extractor = Extractor("non_existent_file")
    assert not extractor.file_exists()
    with tempfile.TemporaryFile(dir=extractor.PATH) as temp:
        name = temp.name.replace("\\", "/").split("/")[-1]
        extractor = Extractor(name)
        assert extractor.file_exists()


def test_archive():
    """Unit test for archive()."""
    open(Extractor.PATH / "dummy", "wb").close()
    extractor = Extractor("dummy")
    archived_file = extractor.archive()
    assert not extractor.file_exists()
    new_location = Path(archived_file)
    assert new_location.exists()
    new_location.unlink()
