"""Tests for the RealEstateParser class."""
from datetime import datetime
from parsers.real_estate_parser import RealEstateParser


def test_parse():
    """Unit test for parse()"""
    parser = RealEstateParser(None, datetime(2020, 1, 1))
    parser.properties = [["a", 2010, 1000, 5]]
    parser.parse()
    assert parser.parsed_data[0].market_value == 500
