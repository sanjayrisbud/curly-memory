"""Defines the PortfolioAllocationCharts class."""
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

from charts.chart import Chart


class PortfolioAllocationCharts(Chart):
    """Class to create chart to plot portfolio allocation by share count and total cost."""

    def draw_chart(self):
        """Draw a chart to represent the data."""
        symbols, labels1, shares, labels2, prices, colors = self.derive_datapoints()

        figure, (axis1, axis2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
        wedges, *_ = axis1.pie(
            shares,
            autopct=lambda x: f"{x:.2f}%" if x > 3 else "",
            labels=labels1,
            colors=colors,
        )
        axis2.pie(
            prices,
            autopct=lambda x: f"{x:.2f}%" if x > 3 else "",
            labels=labels2,
            colors=colors,
        )

        axis1.legend(
            wedges,
            symbols,
            title="Stocks",
            loc="center left",
            bbox_to_anchor=(1.0, 0, 0, 1),
        )
        axis1.set_title("Allocation by share count")
        axis2.set_title("Allocation by total cost")

        return figure

    def derive_datapoints(self):
        """Get the data points for the chart."""
        stocks = self.data[1].get("Portfolio", {}).get("records", [])
        symbols = [record.stock for record in stocks]
        shares = [record.shares for record in stocks]
        prices = [record.total_cost for record in stocks]

        # slight modification to code in
        # https://matplotlib.org/stable/gallery/color/named_colors.html
        by_hsv = sorted(
            (tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))), name)
            for name, color in mcolors.CSS4_COLORS.items()
            if "green" in name or "blue" in name
        )
        colors = sorted([name for hsv, name in by_hsv])

        labels1 = [
            symbol if 100 * share / np.sum(shares) > 1 else " "
            for symbol, share in zip(symbols, shares)
        ]

        labels2 = [
            symbol if 100 * price / np.sum(prices) > 2 else " "
            for symbol, price in zip(symbols, prices)
        ]

        return symbols, labels1, shares, labels2, prices, colors
