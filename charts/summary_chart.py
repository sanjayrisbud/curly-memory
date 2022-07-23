"""Defines the SummaryChart class."""
import matplotlib.pyplot as plt
import numpy as np

from charts.chart import Chart


class SummaryChart(Chart):
    """Class to create a chart to plot summary data."""

    def draw_chart(self):
        """Draw a chart to represent the data."""
        assets, liabilities, net_worth, xpoints = self._derive_datapoints()

        figure, axis = plt.subplots()
        axis.plot(xpoints, assets, label="Assets")
        axis.plot(xpoints, liabilities, label="Liabilities")
        axis.plot(xpoints, net_worth, label="Net Worth")
        axis.set_xlabel("Dates")
        axis.set_ylabel("Pesos")
        axis.set_title("Assets vs Liabilities vs Net Worth")
        axis.legend()
        return figure

    def _derive_datapoints(self):
        """Get the datapoints to plot iin the chart."""
        self.db_interface.get_time_series_summary()
        xpoints = np.array([1, 2, 3, 4])
        assets = xpoints * 2
        liabilities = np.sin(xpoints)
        net_worth = assets - liabilities
        return assets, liabilities, net_worth, xpoints
