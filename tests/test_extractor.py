""" Tests for Extractor class. """

import pytest

from extractors.extractor import Extractor


def test_is_stale(writable_path):
    """Unit test for is_stale()."""
    extractor = Extractor("dummy", writable_path)
    with open(extractor.path / "dummy", "wb") as _:
        pass
    assert not extractor.is_stale()
    extractor.file_object.unlink()


def test_extract(writable_path):
    """Unit test for extract()."""
    extractor = Extractor("dummy", writable_path)
    with pytest.raises(NotImplementedError):
        extractor.extract()
