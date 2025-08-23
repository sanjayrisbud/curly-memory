"""Defines RealEstateParser class."""
from models.real_estate import RealEstate
from parsers.parser import Parser


class RealEstateParser(Parser):
    """Parser for real estate."""

    def __init__(self, path, date):
        super().__init__(path, date)
        self.properties = [
            ["Unit 616 Rockfort Residences, Makati", 2014, 1_800_000, 0],
            [
                "Unit 1007 Tower 1, Avida Towers One Union Place, Taguig",
                2019,
                2_500_000,
                0,
            ],
        ]

    def parse(self):
        """Parse the real estate information."""
        for property_ in self.properties:
            record = RealEstate(self.date, *property_)
            record.compute_market_value(
                age_in_years=self.date.year - record.year_bought
            )
            self.parsed_data.append(record)
            self.total_amount += record.market_value
