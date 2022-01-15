"""Tests for WebpageExtractor class."""
from pathlib import Path

from extractors.pdf_extractor import PDFExtractor


def test_extract():
    """Unit test for extract()."""
    path = Path(__file__).parent / "files"
    pdf = PDFExtractor("dummy.pdf", path)
    assert pdf.file_exists()
    assert pdf.file_type == "pdf"

    pdf.extract()
    assert isinstance(pdf.raw_data, list)
