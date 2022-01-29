"""Tests for the InsurancePoliciesParser class."""

from parsers.insurance_policies_parser import InsurancePoliciesParser


def test_parse():
    """Unit test for parse()"""
    parser = InsurancePoliciesParser("dummy", None, None)
    temp = [
        "12/31/21, 4:47 PM Sun Life Financial - Philippines",
        "Summary of accounts",
        "CUSTOMIZE ACCOUNT LIST",
        "()",
        "Life Policies",
        "SANJAY RISBUD",
        "MY ACCOUNT Policy number Policy name Status Face amount",
        "\uf03a   All",
        "0123456 SUN CLASSIC LIFE Paid-up PHP 607",
        "\uf0e9   Life ()",
        "This site uses cookies to provide the best experience possible. ",
        "(http://www.sunlife.com/PSLF/philippines/Privacy/Our+online+policy?vgnLocale=en_CA).",
        "https://mobile.sunlife.com.ph/Sunlife/apps/services/www/Sunlife 1/1",
    ]
    parser.extractor.raw_data = ["\n".join(temp)]
    parser.parse()
    assert parser.parsed_data[0].balance == 607
