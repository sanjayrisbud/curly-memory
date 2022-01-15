"""Defines the PDFExtractor class."""

import pdfplumber

from extractors.extractor import Extractor


class PDFExtractor(Extractor):
    """Class for extracting data from PDFs."""

    def __init__(self, filename, path=None, date=None):
        super().__init__(filename, path, date)
        self.file_type = "pdf"

    def extract(self):
        """Return a list object containing the data in the PDF."""
        with pdfplumber.open(self.file_object) as pdf:
            self.raw_data = [p.extract_text() for p in pdf.pages]
