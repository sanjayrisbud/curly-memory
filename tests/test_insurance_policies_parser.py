"""Tests for the InsurancePoliciesParser class."""
from bs4 import BeautifulSoup
from parsers.insurance_policies_parser import InsurancePoliciesParser


def test_parse():
    """Unit test for parse()"""
    parser = InsurancePoliciesParser("dummy", None, None)
    temp = """
								<tr ng-repeat="policy in lifePolicies track by $index">
									<td><span class="ng-binding">0800261739</span> 
                                    </td>
									<td><span class="ng-binding">SUN CLASSIC LIFE </span></td>
									<td><span class="ng-binding">Paid-up</span></td>
									<td class="last">
										<label class="control control--checkbox">
											<input type="checkbox" id="lifeChk0" ng-model="life[$index]" ng-true-value="'N'" ng-false-value="'Y'" ng-change="stateChange(life)" class="ng-pristine ng-untouched ng-valid">
											<div class="control__indicator checked" id="life0" ng-class="{'checked': life[$index] == 'N'}"></div>
										</label>
									</td>
								</tr>
    """
    parser.extractor.raw_data = BeautifulSoup(temp)
    parser.parse()
    assert parser.parsed_data[0].balance == 25_000
