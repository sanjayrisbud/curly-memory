"""Tests for the MutualFundsParser class."""

from parsers.mutual_funds_parser import MutualFundsParser


def test_parse():
    """Unit test for parse()"""
    parser = MutualFundsParser("dummy", None, None)
    temp = [
        "12/31/21, 5:47 PM Sun Life Financial - Philippines",
        "Summary of accounts",
        "CUSTOMIZE ACCOUNT LIST",
        "()",
        "Life Policies",
        "SANJAY RISBUD",
        "00406538CF01 PESO STARTER FUND PHP 10.00 Individual",
        "00406538CF01 DOLLAR STARTER FUND PHP 0.00 Individual",
        "\uf00d",
        "This site uses cookies to provide the best experience possible.",
    ]
    parser.extractor.raw_data = ["\n".join(temp)]
    parser.parse()
    assert parser.parsed_data[0].mkt_value == 10
    assert parser.parsed_data[1].mkt_value == 0
