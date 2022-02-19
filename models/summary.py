"""Defines Summary class."""
from sqlalchemy import Column, Float, String
from models import Base, ModelsParent


class Summary(Base, ModelsParent):
    """Model for stock/mutual fund position."""

    __tablename__ = "summaries"
    title = Column(String(50))
    value = Column(Float)

    def __init__(self, date, title, value):
        self.date = date
        self.title = title
        self.value = value

    def __str__(self):
        return self.title + "-->" + str(self.value)
