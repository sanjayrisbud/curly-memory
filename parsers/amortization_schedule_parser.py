"""Defines the AmortizationScheduleParser class."""

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
        amorts = soup.find("tbody", id="amort_sched")
        for row in amorts.find_all("tr"):
            fields = [
                td.text.strip().replace("$", "").replace(",", "")
                for td in row.find_all("td")
            ]
            if fields[0] == "":
                continue
            self.append(AmortizationPayment(*fields))
