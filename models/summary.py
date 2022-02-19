"""Defines Summary class."""
from sqlalchemy import Column, Float, String
from models import Base, ModelsParent


class Summary(Base, ModelsParent):
    """Model for stock/mutual fund position."""

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
