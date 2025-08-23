"""Defines MutualFundsParser class."""
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

        for fund in self.additional_data["mutual_funds"]:
            fund_name = fund["name"]
            fund_shares = fund["shares"]
            market_value = fund["market_value"]
            total_cost = fund["total_cost"]
            company = fund["company"]
            currency = fund["currency"]

            record = StockPosition(
                self.date,
                fund_name,
                fund_shares,
                market_value,
                total_cost,
                company=company
            )

            if currency == "USD":
                record.mkt_value *= self.additional_data["php_to_1_usd"]
                record.total_cost  *= self.additional_data["php_to_1_usd"]

            self.parsed_data.append(record)
            self.total_amount += record.mkt_value
