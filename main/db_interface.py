"""Defines the DatabaseInterface class."""
from datetime import datetime

from models import summary
from models import bank_account
from models import stock_position


class DatabaseInterface:
    """Class used to interface with the database."""

    def __init__(self, db_file, db_engine):
        self._db_file = db_file
        self._db_engine = db_engine
        self.date_from = datetime(2024, 1, 1)

    def archive_db_file(self):
        """Archive the database file."""
        self._db_file.archive()

    def get_previous_financial_data(self):
        """Get previous financial data."""
        previous = summary.Summary.get_date_right_before(
            self._db_engine, date=self._db_file.date
        )[0][0]

        summary_records, _ = self._get_table_prev_data(summary.Summary, date=previous)
        accounts, accounts_total = self._get_table_prev_data(
            bank_account.BankAccount, date=previous
        )
        portfolio, portfolio_total = self._get_table_prev_data(
            stock_position.StockPosition, date=previous
        )

        amortization_schedule_dict = {"AmortizationSchedule": 0}
        credit_card_dict = {"CreditCard": 0}
        if len(summary_records) > 5:
            amortization_schedule = summary_records[5]
            credit_card = summary_records[6]
            amortization_schedule_dict = self._form_dict(
                [amortization_schedule],
                amortization_schedule.value,
            )
            credit_card_dict = self._form_dict([credit_card], credit_card.value)

        return (
            summary_records,
            {
                "BankAccounts": self._form_dict(accounts, accounts_total),
                "Portfolio": self._form_dict(portfolio, portfolio_total),
            },
            {
                "AmortizationSchedule": amortization_schedule_dict,
                "CreditCard": credit_card_dict,
            },
        )

    def _get_table_prev_data(self, model, date):
        """Get the previous data from the database table; sum the records if needed."""
        list_to_return = list(model.find_by_date(self._db_engine, date))
        if model == summary.Summary:
            total = 0
        elif model == bank_account.BankAccount:
            total = sum([account.balance for account in list_to_return])
        else:
            total = sum([stock.mkt_value for stock in list_to_return])
        return list_to_return, total

    def store_various_financial_data(self, financial_data):
        """Store various financial data points in the database for later use."""
        for summ in financial_data[0]:
            summ.insert(self._db_engine)
        for account in financial_data[1]["BankAccounts"]["records"]:
            account.insert(self._db_engine)
        for stock in financial_data[1]["Portfolio"]["records"]:
            stock.insert(self._db_engine)

    def get_time_series_summary(self):
        """Return a summary of asset and liability values as 3 time series."""
        result = summary.Summary.get_asset_and_liability_values(self._db_engine, self.date_from)
        date_points = [row[0] for row in result[0]]
        asset_points = [row[2] for row in result[0]]
        liability_points = [row[2] for row in result[1]]
        return date_points, asset_points, liability_points

    def get_time_series_portfolio(self):
        """Return the portfolio's market price and total cost values as 3 time series."""
        result = stock_position.StockPosition.get_market_values_and_total_costs(
            self._db_engine, self.date_from)
        date_points = [row[0] for row in result]
        market_value_points = [row[1] for row in result]
        total_cost_points = [row[2] for row in result]
        return date_points, market_value_points, total_cost_points


    @staticmethod
    def _form_dict(records, total_amount):
        """Return the parameters as a dict."""
        return {"records": records, "total_amount": total_amount}
