"""Tests for the Parser class."""
import pytest

from parsers.parser import Parser


def test_get_data():
    """Unit test for get_data()."""
    parser = Parser()
    with pytest.raises(Exception):
        parser.get_data()


def test_parse():
    """Unit test for parse()."""
    parser = Parser()
    with pytest.raises(NotImplementedError):
        parser.parse()


def test_append():
    """Unit test for append()."""
    parser = Parser()
    parser.append("model")
    assert len(parser.parsed_data) == 1
