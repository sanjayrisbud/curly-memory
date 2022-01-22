"""Tests for the BankAccountsParser class."""

from parsers.bank_accounts_parser import BankAccountsParser


def test_parse():
    """Unit test for parse()"""
    parser = BankAccountsParser("dummy", None, None)
    temp = [
        "1/8/22, 3:25 PM BPI Online",
        "M G \uf0e0",
        "Deposits (1)",
        "\uf105",
        "Salary",
        "1234567890",
        " 607",
        "PHP .35",
        "Manage My Accounts",
        "https://online.bpi.com.ph/portalserver/onlinebanking/my-accounts 1/1",
    ]
    parser.extractor.raw_data = ["\n".join(temp)]
    parser.parse()
    assert parser.parsed_data[0].balance == 607
