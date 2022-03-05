"""Initialize the database and define models' base classes."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Column, DateTime, Integer


Base = declarative_base()


class ModelsParent:
    """Base class for all database models."""

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)

    def insert(self, engine):
        """Add a single object to the database."""
        with Session(engine) as session:
            session.add(self)
            session.commit()
            object_id = self.id
        return object_id

    @staticmethod
    def insert_many(engine, records):
        """Add multiple objects to the database."""
        with Session(engine) as session:
            session.add_all(records)
            session.commit()
            object_ids = [record.id for record in records]
        return object_ids

    @classmethod
    def find_by_date(cls, engine, date):
        """Find records written on a certain date."""
        with Session(engine) as session:
            result = session.query(cls).filter(cls.date == date)
        return result


def get_engine(full_path, create_db):
    """Create database engine (and tables if necessary)"""
    engine = create_engine("sqlite:///" + full_path, echo=True)

    if create_db:
        from models.summary import Summary
        from models.stock_position import StockPosition
        from models.bank_account import BankAccount

        Base.metadata.create_all(engine)

    return engine
