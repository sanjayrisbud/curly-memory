"""Module to declare test fixtures."""
import pytest
import models


@pytest.fixture()
def writable_path():
    """Return a dummy writable path."""
    return r"C:\Users\sanjay s risbud\Dropbox\statements\tests"


@pytest.fixture()
def engine(writable_path):
    """Return a dummy database engine."""
    return models.get_engine(writable_path + "/db.sqlite3", create_db=True)
