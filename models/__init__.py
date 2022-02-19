"""Initialize the database and define models' base classes."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, DateTime, Integer


class ModelsParent:
    """Base class for all database models."""

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)

    def insert(self):
        """Add a single object to the database."""
        with Session(engine) as session:
            session.add(self)
            session.commit()
            object_id = self.id
        return object_id

    @staticmethod
    def insert_many(records):
        """Add multiple objects to the database."""
        with Session(engine) as session:
            session.add_all(records)
            session.commit()
            object_ids = [record.id for record in records]
        return object_ids

    @classmethod
    def find_by_date(cls, date):
        """Find records written on a certain date."""
        with Session(engine) as session:
            result = session.query(cls).filter(cls.date == date)
        return result


engine = create_engine("sqlite:///db.sqlite3", echo=True)

Base = declarative_base()

from models.summary import Summary  # pylint: disable=wrong-import-position
from models.stock_position import StockPosition  # pylint: disable=wrong-import-position
from models.bank_account import BankAccount  # pylint: disable=wrong-import-position

Base.metadata.create_all(engine)
