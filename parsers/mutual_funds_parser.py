"""Defines MutualFundsParser class."""
from extractors.pdf_extractor import PDFExtractor
from models.stock_position import StockPosition
from parsers.parser import Parser


class MutualFundsParser(Parser):
    """Parser for the mutual funds."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = PDFExtractor(filename, self.path, self.date)

    def parse(self):
        """Parse the mutual funds' information."""
        lines = self.extractor.raw_data[0].split("\n")

        # get only fund-relevant lines and clean up each one
        fund_lines = [
            line.replace("PHP", "")
            .replace("USD", "")
            .replace("Individual", "")[line.index("0") :]
            .strip()
            for line in lines
            if "00406538CF01" in line
        ]

        for line in fund_lines:
            _, *fund_name, market_value = line.split(" ")

            record = StockPosition(
                self.date,
                " ".join(fund_name).strip(),
                "0",
                market_value.replace(",", ""),
                market_value.replace(",", ""),
            )

            # simply set the peso->dollar rate to 50->1
            if fund_name[0].startswith("DOLLAR"):
                record.mkt_value *= 50
                record.total_cost = record.mkt_value

            self.parsed_data.append(record)
            self.total_amount += record.mkt_value
