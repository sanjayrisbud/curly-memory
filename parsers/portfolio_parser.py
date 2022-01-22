"""Defines the PortfolioParser class."""
import math
from extractors.webpage_extractor import WebpageExtractor
from models.stock_position import StockPosition
from parsers.parser import Parser


class PortfolioParser(Parser):
    """Parser for the stock portfolio."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = WebpageExtractor(filename, self.path, self.date)

    def parse(self):
        """Parse the portfolio."""
        soup = self.extractor.raw_data
        stocks = soup.find("ul", id="SpDataItemList")
        for row in stocks.find_all("li"):
            fields = [
                div.text.strip().replace("$", "").replace(",", "")
                for div in row.find_all("div")
            ]
            record = StockPosition(
                self.date, fields[1], fields[4], fields[5], fields[6]
            )
            self.total_amount += record.mkt_value
            self.append(record)

        self.total_amount = math.floor(self.total_amount)
