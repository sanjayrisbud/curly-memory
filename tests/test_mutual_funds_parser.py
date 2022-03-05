"""Tests for the MutualFundsParser class."""
from datetime import datetime
from bs4 import BeautifulSoup

from parsers.mutual_funds_parser import MutualFundsParser


def test_parse(writable_path):
    """Unit test for parse()"""
    parser = MutualFundsParser("dummy", writable_path, datetime.today())
    temp = """
                                <tr ng-repeat="fund in mutualFunds track by $index">
									<td><span class="ng-binding">00406538CF01</span></td>
									<td><span class="ng-binding">PESO STARTER FUND</span></td>
									<td><span class="ng-binding">0.00</span></td>
									<td><span class="ng-binding">1.3186</span></td>
									<td><span class="ng-binding">PHP 10.00</span></td>
									<td class="last">
										<label class="control control--checkbox">
											<input type="checkbox" id="mfChk3" ng-model="mf[$index]" ng-true-value="'N'" ng-false-value="'Y'" ng-change="stateChange(mf)" class="ng-pristine ng-untouched ng-valid">
											<div class="control__indicator checked" id="mf3" ng-class="{'checked': mf[$index] == 'N'}"></div>
										</label>
									</td>
								</tr>
    """
    parser.extractor.raw_data = BeautifulSoup(temp)
    parser.parse()
    assert parser.parsed_data[0].mkt_value == 10
