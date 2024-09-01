"""Defines the AllocationCharts class."""
import matplotlib.pyplot as plt

from charts.chart import Chart


class AllocationCharts(Chart):
    """
    Class to create charts to plot allocations:
        1. Breakdown: All summary entries
        2. Assets by class
            - solid: real estate + insurance policies
            - liquid: bank accounts - credit card - amortization schedule
            - gas: portfolio + mutual fund
        3. Liquid vs Gas
    """

    def draw_chart(self):
        """Draw a chart to represent the data."""
        data_for_charts = self.derive_datapoints()
        count_of_charts = len(data_for_charts)

        # Creating plots
        figure, axes = plt.subplots(nrows=count_of_charts, ncols=1,
                                    figsize=(3, 2 * count_of_charts))

        for axis, data_for_chart in zip(axes, data_for_charts):
            title, names, values, explode, colors, legend = data_for_chart
            wedges, *_ = axis.pie(values,
                                  autopct=lambda pct: f"{pct:.1f}%" if pct > 1 else "",
                                  explode=explode,
                                  labels=names,
                                  shadow=True,
                                  colors=colors,
                                  startangle=45,
                                  textprops={"fontsize": 8},
                                  wedgeprops={"linewidth": 1, "edgecolor": "black"},
                                  )
            axis.legend(wedges, legend, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
            axis.set_title(title)

        return figure

    def derive_datapoints(self):
        """Get the data points for the chart."""
        entries = self.data[0]

        names_1 = []
        names_2 = ["", "", ""]
        names_3 = ["", ""]

        values_1 = []
        solid = liquid = gas = 0

        title_1 = "Breakdown"
        title_2 = "Assets by Class"
        title_3 = "Liquid vs Gas"

        colors_1 = ["green", "yellow", "cyan", "lightgrey", "blue", "magenta", "red"]
        colors_2 = ["steelblue", "seagreen", "orange"]
        colors_3 = ["seagreen", "orange"]

        explode_1 = (0.1, 0.0, 0.4, 0.2, 0.1, 0.1, 0.1)
        explode_2 = (0.1, 0.0, 0.2)
        explode_3 = (0.1, 0.1)

        legend_1 = []
        legend_2 = [
            "Solid: Real Estate + Insurance Policies",
            "Liquid: Cash - Credit Card Bill - Amortization Due",
            "Gas: Portfolio + Mutual Funds"
        ]
        legend_3 = [
            "Liquid: Cash - Credit Card Bill - Amortization Due",
            "Gas: Portfolio + Mutual Funds"
        ]

        for entry in entries:
            key = entry.title
            val = entry.value if entry.entry_type == "ASSET" else 0 - entry.value
            names_1.append("")
            legend_1.append(key)
            values_1.append(abs(val))
            if key in ("InsurancePolicies", "RealEstate"):
                solid += val
            elif key in ("Portfolio", "MutualFunds"):
                gas += val
            else:
                liquid += val

        for_chart_1 = (title_1, names_1, values_1, explode_1, colors_1, legend_1)
        for_chart_2 = (title_2, names_2, [solid, liquid, gas], explode_2, colors_2, legend_2)
        for_chart_3 = (title_3, names_3, [liquid, gas], explode_3, colors_3, legend_3)

        return for_chart_1, for_chart_2, for_chart_3
