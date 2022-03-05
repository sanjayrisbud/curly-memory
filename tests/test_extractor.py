""" Tests for Extractor class. """

import pytest

from extractors.extractor import Extractor


def test_is_stale(stmt_path):
    """Unit test for is_stale()."""
    extractor = Extractor("dummy", stmt_path)
    with open(extractor.path / "dummy", "wb") as _:
        pass
    assert not extractor.is_stale()
    extractor.file_object.unlink()


def test_extract(stmt_path):
    """Unit test for extract()."""
    extractor = Extractor("dummy", stmt_path)
    with pytest.raises(NotImplementedError):
        extractor.extract()
