"""Module to declare test fixtures."""
import pytest


@pytest.fixture()
def stmt_path():
    """Return the folder containing the statements."""
    return r"C:\Users\sanjay s risbud\Dropbox\statements\tests"
