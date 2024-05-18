"""Defines the SummaryChart class."""
import matplotlib.pyplot as plt
import numpy as np
from charts.chart import Chart


class SummaryChart(Chart):
    """Class to create a chart to plot summary data."""

    def draw_chart(self):
        """Draw a chart to represent the data."""
        assets, liabilities, net_worth, xpoints = self.derive_datapoints()

        figure, axis = plt.subplots()
        figure.set_size_inches(12, 5.6)
        figure.autofmt_xdate(rotation=45)

        axis.plot(xpoints, assets, "b^--", label="Assets")
        axis.plot(xpoints, liabilities, "r*--", label="Liabilities")
        axis.plot(xpoints, net_worth, "go-", label="Net Worth")
        axis.set_xlabel("Dates")
        axis.set_ylabel("PHP")
        axis.set_yticks(list(range(0, 15_000_000, 1_000_000)))
        axis.yaxis.set_major_formatter("{x:,}")
        axis.set_title("Assets vs Liabilities vs Net Worth")
        axis.grid(True)
        axis.legend()
        return figure

    def derive_datapoints(self):
        """Get the data points to plot in the chart."""
        xpoints, assets, liabilities = self.db_interface.get_time_series_summary()
        xpoints = [xpoint.strftime("%m/%d/%Y") for xpoint in xpoints]
        net_worth = np.array(assets) - np.array(liabilities)
        return assets, liabilities, net_worth, xpoints
