"""Tests for the PortfolioParser class."""
from datetime import datetime
from bs4 import BeautifulSoup
from parsers.portfolio_parser import PortfolioParser


def test_parse(writable_path):
    """Unit test for parse()"""
    parser = PortfolioParser("dummy", writable_path, datetime.today())
    html = """<ul id="SpDataItemList"><li>
		<div><a>BUY</a>&nbsp;|<a>SELL</a></div>
		<div>					AC							</div>
		<div>					868.00				</div>
		<div>					702.0652			</div>
		<div>					70				</div>
		<div>					60,216.20					</div>
		<div>					49,144.56				</div>
		<div>	+11,071.63	</div>
		<div>	+22.53%	</div>
            </li></ul>"""
    parser.extractor.raw_data = BeautifulSoup(html, "html.parser")
    parser.parse()
    assert parser.parsed_data[0].shares == 70
