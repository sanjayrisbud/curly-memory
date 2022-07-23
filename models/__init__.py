"""Initialize the database and define models' base classes."""

# pylint: disable=import-outside-toplevel, unused-import, cyclic-import

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
        with self.get_session(engine) as session:
            session.add(self)
            session.commit()
            object_id = self.id
        return object_id

    @classmethod
    def insert_many(cls, engine, records):
        """Add multiple objects to the database."""
        with cls.get_session(engine) as session:
            session.add_all(records)
            session.commit()
            object_ids = [record.id for record in records]
        return object_ids

    @classmethod
    def find_by_date(cls, engine, date):
        """Find records written on a certain date."""
        with cls.get_session(engine) as session:
            result = session.query(cls).filter(cls.date == date)
        return result

    @staticmethod
    def get_session(engine):
        """Return a database session object."""
        return Session(engine)


def get_engine(full_path):
    """Create database engine."""
    engine = create_engine("sqlite:///" + full_path, echo=True)
    return engine
