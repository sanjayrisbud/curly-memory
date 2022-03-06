"""Module to declare test fixtures."""
import pytest
import models

WRITABLE_PATH = r"C:\Users\sanjay s risbud\Dropbox\statements\tests"


@pytest.fixture()
def writable_path():
    """Return a dummy writable path."""
    return WRITABLE_PATH


@pytest.fixture()
def engine():
    """Return a dummy database engine."""
    return models.get_engine(WRITABLE_PATH + "/db.sqlite3")
