"""Defines StockPosition class."""
from sqlalchemy import Column, Float, Integer, String, func
from models import Base, ModelsParent


class StockPosition(Base, ModelsParent):
    """Model for stock/mutual fund position."""

    __tablename__ = "stocks"
    stock = Column(String(10))
    shares = Column(Integer)
    mkt_value = Column(Float)
    total_cost = Column(Float)

    def __init__(self, *args):
        date, stock, shares, mkt_value, total_cost = args
        self.date = date
        self.stock = stock
        self.shares = int(shares)
        self.mkt_value = float(mkt_value)
        self.total_cost = float(total_cost)

    def neither_bought_nor_sellable(self):
        """Return True if the shares were neither bought nor sellable."""
        return self.mkt_value == 0 or self.total_cost == 0

    def compute_profit_or_loss(self):
        """Compute for the amount of profit or loss."""
        return (
            0
            if self.neither_bought_nor_sellable()
            else self.mkt_value - self.total_cost
        )

    def compute_pct_profit_or_loss(self):
        """Compute for the percentage of profit or loss."""
        return (
            0
            if self.neither_bought_nor_sellable()
            else 100 * self.compute_profit_or_loss() / self.total_cost
        )

    def get_status(self):
        """Get the status in this stock."""
        if self.neither_bought_nor_sellable():
            return "unknown"

        value = self.compute_profit_or_loss()
        if value > 0:
            return "gain"
        if value < 0:
            return "loss"
        return "break even"

    def __str__(self):
        return self.stock + "-->" + str(self.mkt_value)

    @classmethod
    def get_market_values_and_total_costs(cls, engine):
        """Return market values and total costs, sorted by ascending date."""
        with cls.get_session(engine) as session:
            return (
                session.query(
                    cls.date, func.sum(cls.mkt_value), func.sum(cls.total_cost)
                )
                .group_by(cls.date)
                .order_by(cls.date)
            )
