"""Tests for the Parser class."""
import pytest
from datetime import datetime
from parsers.parser import Parser


def test_get_data(writable_path):
    """Unit test for get_data()."""
    parser = Parser(writable_path, datetime.today())
    with pytest.raises(Exception):
        parser.get_data()


def test_parse(writable_path):
    """Unit test for parse()."""
    parser = Parser(writable_path, datetime.today())
    with pytest.raises(NotImplementedError):
        parser.parse()


def test_append(writable_path):
    """Unit test for append()."""
    parser = Parser(writable_path, datetime.today())
    parser.append("model")
    assert len(parser.parsed_data) == 1
