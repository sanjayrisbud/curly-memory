"""Defines the AmortizationScheduleParser class."""
import datetime

from extractors.webpage_extractor import WebpageExtractor
from models.amortization_payment import AmortizationPayment
from parsers.parser import Parser


class AmortizationScheduleParser(Parser):
    """Parser for the amortization schedule."""

    def __init__(self, filename, path, date):
        super().__init__(path, date)
        self.extractor = WebpageExtractor(filename, self.path, self.date)

    def parse(self):
        """Parse the webpage data."""
        soup = self.extractor.raw_data
        self.parsed_data.append(None)
        amorts = soup.find("tbody", id="amort_sched")
        for row in amorts.find_all("tr"):
            fields = [
                td.text.strip().replace("$", "").replace(",", "")
                for td in row.find_all("td")
            ]
            if fields[0] == "":
                continue
            record = AmortizationPayment(*fields)
            if self.date > record.date:
                self.total_amount = record.balance
                self.parsed_data[0] = record
            else:
                # loan has been fully paid
                record.date = datetime.datetime(year=2023, month=4, day=20)
                record.principal = record.amount = 1_539_274.71
                record.interest = record.balance = self.total_amount = 0
                self.parsed_data[0] = record
                break
