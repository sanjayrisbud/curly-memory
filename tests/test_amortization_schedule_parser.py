"""Tests for the AmortizationScheduleParser class."""
from datetime import datetime
from bs4 import BeautifulSoup
from parsers.amortization_schedule_parser import AmortizationScheduleParser


def test_parse(writable_path):
    """Unit test for parse()"""
    parser = AmortizationScheduleParser("dummy", writable_path, datetime.today())
    html = """<tbody id="amort_sched"><tr><td colspan="6"></td></tr>
    <tr>
        <td>1</td>
        <td>Jul 1, 2018</td>
        <td>$10</td>
        <td>$6</td>
        <td>$4</td>
        <td>$1</td>
    </tr></tbody>"""
    parser.extractor.raw_data = BeautifulSoup(html, "html.parser")
    parser.parse()
    assert parser.parsed_data[0].payment_number == 1
