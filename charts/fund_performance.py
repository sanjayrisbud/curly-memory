"""Defines the FundPerformanceChart class."""
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

from charts.chart import Chart


class FundPerformanceChart(Chart):
    """Class to create a chart to plot fund performance."""

    def draw_chart(self):
        """Draw a chart to represent the data."""
        funds_list, xpoints_list, ratios_list = self.derive_datapoints()
        line_colors = [name for name in mcolors.TABLEAU_COLORS]

        figure, axis = plt.subplots()
        figure.set_size_inches(12, 5.6)
        figure.autofmt_xdate(rotation=45)
        axis.set_ylim(0.8, 1.5)

        for i, fund in enumerate(funds_list):
            axis.plot(xpoints_list[i], ratios_list[i], line_colors[i], label=fund)
        axis.set_xlabel("Dates")
        axis.set_ylabel("Market Value / Total Cost")
        axis.set_yticks([x/9 + 0.7 for x in range(10)])
        axis.yaxis.set_major_formatter("{x:.1f}")
        axis.set_title("Comparison of Fund Performances")
        axis.grid(True)
        axis.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        return figure

    def derive_datapoints(self):
        """Get the data points to plot in the chart."""
        fund_names = ["PORTFOLIO"]
        fund_names.extend([fund["name"]
                      for fund in
                      self.data[3]["mutual_funds"]])

        xpoints_list = []
        ratios_list = []
        for _, fund_name in enumerate(fund_names):
            (
                xpoints,
                market_values,
                total_costs,
                counts
            ) = self.db_interface.get_time_series_of_market_values_and_total_costs(fund_name)
            xpoints_list.append([xpoint.strftime("%m/%d/%Y") for xpoint in xpoints])
            ratios_list.append(np.array(market_values)/np.array(total_costs))

        return fund_names, xpoints_list, ratios_list
