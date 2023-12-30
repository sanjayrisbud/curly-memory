"""Defines Summary class."""
from sqlalchemy import Column, Float, String, func
from models import Base, ModelsParent


class Summary(Base, ModelsParent):
    """Model for summary data."""

    __tablename__ = "summaries"
    entry_type = Column(String(50))
    title = Column(String(50))
    value = Column(Float)

    def __init__(self, date, entry_type, title, value):
        self.date = date
        self.entry_type = entry_type
        self.title = title
        self.value = value

    def __str__(self):
        return self.title + "-->" + str(self.value)

    @classmethod
    def get_asset_and_liability_values(cls, engine, date_from):
        """Return asset and liability values, sorted by ascending date."""
        with cls.get_session(engine) as session:
            assets = cls.query_by_entry_type(session, "ASSET", date_from)
            liabilities = cls.query_by_entry_type(session, "LIABILITY", date_from)
        return assets, liabilities

    @classmethod
    def query_by_entry_type(cls, session, entry_type, date_from):
        """Return the result of querying the summary by entry type."""
        return (
            session.query(cls.date, cls.entry_type, func.sum(cls.value))
            .filter(cls.entry_type == entry_type)
            .filter(cls.date >= date_from)
            .group_by(cls.date, cls.entry_type)
            .order_by(cls.date, cls.entry_type)
        )

    @classmethod
    def get_date_right_before(cls, engine, date):
        """Get fetch date immediately before the given date."""
        with cls.get_session(engine) as session:
            previous = session.query(func.max(cls.date)).filter(cls.date < date)
        return previous
