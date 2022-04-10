"""Tests for the MutualFundsParser class."""
from datetime import datetime
from bs4 import BeautifulSoup

from parsers.mutual_funds_parser import MutualFundsParser


def test_parse(writable_path):
    """Unit test for parse()"""
    parser = MutualFundsParser("dummy", writable_path, datetime.today())
    temp = """
                                <tr ng-repeat="fund in filteredMutualFunds = (mutualFunds | filter: {hide: 'N'}) | limitTo:mutualFundsLimit">
                                    <td>
                                        <a ui-sref="dashboard.accounts.mf({accountNumber: fund.accountNumber, fundCode: fund.fundCode})" class="ng-binding" href="#/dashboard/accounts/mutual-fund/00406538CF01/CF0002">00406538CF01</a> 
                                    </td>
                                    <td class="ng-binding">BALANCED FUND</td>
                                    <td class="ng-binding">PHP 10.00</td>
                                    <td class="ng-binding">Individual</td>
                                </tr>    """
    parser.extractor.raw_data = BeautifulSoup(temp, "html.parser")
    parser.parse()
    assert parser.parsed_data[0].mkt_value == 10
