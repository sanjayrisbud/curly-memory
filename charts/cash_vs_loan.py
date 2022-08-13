"""Defines the CashVsLoanChart class."""
import matplotlib.pyplot as plt
import numpy as np

from charts.chart import Chart


class CashVsLoanChart(Chart):
    """Class to create a chart to plot cash vs loan amount data."""

    def draw_chart(self):
        """Draw a chart to represent the data."""
        figure, axis = plt.subplots()

        cimb, bayad, checks, perm, loan, categories = self.derive_datapoints()

        axis.bar(categories, cimb, color="g")
        axis.bar(categories, bayad, bottom=cimb, color="b")
        axis.bar(categories, checks, bottom=cimb + bayad, color="y")
        axis.bar(categories, perm, bottom=cimb + bayad + checks, color="m")
        axis.bar(categories, loan, color="r")
        axis.set_ylabel("PHP")
        axis.set_yticks(list(range(0, 2_000_001, 200_000)))
        axis.yaxis.set_major_formatter("{x:,}")
        axis.legend(["CIMB Bank", "Bayad Utang", "Checks", "Permanent"])
        return figure

    def derive_datapoints(self):
        """Get the data points for the chart."""
        categories = ["Cash", "Loan Amount"]

        cimb = bayad = checks = perm = np.array([0, 0])
        accounts = self.data[1]["BankAccounts"]["records"]
        for account in accounts:
            point = np.array([account.balance, 0])
            if account.account_alias == "Bayad Utang":
                bayad = point
            if account.account_alias == "GSave":
                cimb = point
            if account.account_alias == "Permanent":
                perm = point
            if account.account_alias == "Checks":
                checks = point
        loan = np.array([0, self.data[2]["AmortizationSchedule"]["total_amount"]])
        return cimb, bayad, checks, perm, loan, categories
