""" Tests for Extractor class. """

import pytest

from extractors.extractor import Extractor


def test_is_stale():
    """Unit test for is_stale()."""
    extractor = Extractor("dummy")
    with open(extractor.path / "dummy", "wb") as _:
        pass
    assert not extractor.is_stale()
    extractor.file_object.unlink()


def test_extract():
    """Unit test for extract()."""
    extractor = Extractor("dummy")
    with pytest.raises(NotImplementedError):
        extractor.extract()
