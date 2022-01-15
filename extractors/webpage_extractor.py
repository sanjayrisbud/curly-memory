"""Defines the WebpageExtractor class."""

from bs4 import BeautifulSoup

from extractors.extractor import Extractor


class WebpageExtractor(Extractor):
    """Class for extracting data from webpages."""

    def __init__(self, filename, path=None, date=None):
        super().__init__(filename, path, date)
        self.file_type = "html"

    def extract(self):
        """Return a BeautifulSoup object representing the webpage."""
        html = self.file_object.read_text()
        self.raw_data = BeautifulSoup(html, "html.parser")
