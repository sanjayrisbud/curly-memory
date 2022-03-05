"""Test FinancialStatementGenerator class."""
from financial_stmt_generator import FinancialStatementGenerator


def test_run():
    """Unit test for run()."""
    generator = FinancialStatementGenerator()
    generator.run()
    assert generator.asset_parsers[0].total_amount > 0


def test_mine_data():
    """Unit test for mine_data()."""
    generator = FinancialStatementGenerator()
    generator.mine_data()
    assert "credit card" not in vars(generator)


def test_write_statement():
    """unit test for write_statement()."""
    generator = FinancialStatementGenerator()
    generator.write_statement()
    assert vars(generator)["credit_card"] is None