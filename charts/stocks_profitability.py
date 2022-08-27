"""Defines the StocksProfitabilityChart class."""
import matplotlib.pyplot as plt

from charts.chart import Chart


class StocksProfitabilityChart(Chart):
    """Class to create chart to plot profitability of stocks."""

    def draw_chart(self):
        """Draw a chart to represent the data."""
        symbols, percentages, colors = self.derive_datapoints()

        figure, axis = plt.subplots(figsize=(len(symbols) * 0.8, 5))
        axis.bar(symbols, percentages, color=colors, width=0.6)

        axis.tick_params(axis="x", rotation=45)

        for i in range(len(symbols)):
            axis.text(
                i,
                percentages[i] // 2,
                f"{percentages[i]:.0f}%",
                ha="center",
                fontsize="x-small",
                bbox=dict(facecolor="white", alpha=0.5),
            )

        axis.set_axisbelow(True)
        axis.yaxis.grid(color="gray", linestyle="dashed")
        axis.set_title("% Profitability")
        return figure

    def derive_datapoints(self):
        """Get the data points for the chart."""
        stocks = self.data[1].get("Portfolio", {}).get("records", [])
        symbols = [record.stock for record in stocks]
        percentages = [record.compute_pct_profit_or_loss() for record in stocks]
        colors = [
            "seagreen" if percentage > 0 else "maroon" for percentage in percentages
        ]
        return symbols, percentages, colors
