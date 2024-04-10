"""Defines the PortfolioParser class."""
import math
from extractors.csv_extractor import CsvExtractor
from models.stock_position import StockPosition
from parsers.parser import Parser


class PortfolioParser(Parser):
    """Parser for the stock portfolio."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = CsvExtractor(filename, self.path, self.date)

    def parse(self):
        """Parse the portfolio."""
        content = self.extractor.raw_data
        for i, row in enumerate(content):
            if i == 0:  # header row
                continue
            record = StockPosition(
                self.date, row[0], row[2], row[5], row[3]
            )
            record.total_cost *= record.shares  # since only avg buying price per share is shown
            self.total_amount += record.mkt_value
            self.append(record)

        self.total_amount = math.floor(self.total_amount)
