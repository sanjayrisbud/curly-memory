"""Defines the PortfolioPerformanceChart class."""
import matplotlib.pyplot as plt

from charts.chart import Chart


class PortfolioPerformanceChart(Chart):
    """Class to create a chart to plot portfolio performance."""

    def draw_chart(self):
        """Draw a chart to represent the data."""
        market_values, total_costs, xpoints = self.derive_datapoints()

        figure, axis = plt.subplots()
        figure.autofmt_xdate(rotation=45)

        axis.plot(xpoints, market_values, "indigo", label="Market Value")
        axis.plot(xpoints, total_costs, "orange", label="Total Cost")
        axis.set_xlabel("Dates")
        axis.set_ylabel("PHP")
        axis.set_yticks(list(range(700_000, 2_000_001, 200_000)))
        axis.yaxis.set_major_formatter("{x:,}")
        axis.set_title("Market Value vs Total Cost")
        axis.grid(True)
        axis.legend()
        return figure

    def derive_datapoints(self):
        """Get the data points to plot in the chart."""
        (
            xpoints,
            market_values,
            total_costs,
        ) = self.db_interface.get_time_series_portfolio()
        xpoints = [xpoint.strftime("%m/%d/%Y") for xpoint in xpoints]
        return market_values, total_costs, xpoints
