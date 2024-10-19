"""Defines MutualFundsParser class."""
import re
from extractors.webpage_extractor import WebpageExtractor
from models.stock_position import StockPosition
from parsers.parser import Parser


class MutualFundsParser(Parser):
    """Parser for the mutual funds."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = WebpageExtractor(filename, self.path, self.date)

    def parse(self):
        """Parse the mutual funds' information."""
        fund_rows = self.extractor.raw_data.find_all(
            "tr", attrs={"ng-repeat": re.compile(r".*fund.*")}
        )

        for fund in fund_rows:
            tds = fund.find_all("td")
            fund_name = tds[1].text.strip()
            fund_shares = 0
            market_value = float(
                tds[4]
                .text.replace(",", "")
                .replace("PHP", "")
                .replace("USD", "")
                .strip()
            )

            record = StockPosition(
                self.date,
                fund_name,
                fund_shares,
                market_value,
                market_value,
            )

            if record.mkt_value == 0:
                continue

            # simply set the peso->dollar rate to 50->1
            if fund_name.startswith("DOLLAR"):
                record.mkt_value *= 55
                record.total_cost = record.mkt_value

            self.parsed_data.append(record)
            self.total_amount += record.mkt_value
