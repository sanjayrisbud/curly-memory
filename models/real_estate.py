"""Defines RealEstate class."""


class RealEstate:
    """Model for real estate."""

    def __init__(self, *args):
        date, address, year_bought, price, depreciation_factor = args
        self.date = date
        self.address = address
        self.year_bought = year_bought
        self.price = self.market_value = price
        self.depreciation_factor = depreciation_factor

    def compute_market_value(self, age_in_years):
        """Compute property value, considering depreciation."""
        yearly_depreciation = (self.depreciation_factor / 100) * self.price
        self.market_value = self.price - age_in_years * yearly_depreciation

    def __str__(self):
        """String equivalent of object."""
        return f"{self.address} (acquired {self.year_bought}) --> {self.market_value}"
