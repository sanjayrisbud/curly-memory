"""Tests for WebpageExtractor class."""
from pathlib import Path
from bs4 import BeautifulSoup

from extractors.webpage_extractor import WebpageExtractor


def test_extract():
    """Unit test for extract()."""
    path = Path(__file__).parent.parent / "files"
    webpage = WebpageExtractor("dummy.html", path)
    assert webpage.file_exists()
    assert webpage.file_type == "html"

    webpage.extract()
    assert isinstance(webpage.raw_data, BeautifulSoup)
