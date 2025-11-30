from . import t
from flet import (
    BarChartGroup,
    BarChartRod,
    BarChart,
    LineChartDataPoint,
    LineChart,
    LineChartData,
    # MatplotlibChart,
    PieChartSection,
    PieChart,
    # PlotlyChart
)


def generate_bar_chart_component(options: t.Options) -> t.Any:
    data = options.get("data", [])
    bar_groups = [
        BarChartGroup(
            x=i,
            bar_rods=[BarChartRod(to_y=value)]
        )
        for i, value in enumerate(data)
    ]
    return BarChart(
        bar_groups=bar_groups,
        tooltip_bgcolor=options.get("tooltip_bgcolor"),
        border=options.get("border"),
    )


def generate_line_chart_component(options: t.Options) -> t.Any:
    data = options.get("data", [])
    points = [LineChartDataPoint(i, value) for i, value in enumerate(data)]
    return LineChart(
        data_series=[
            LineChartData(
                data_points=points,
                color=options.get("color"),
                stroke_width=options.get("stroke_width", 2),
            )
        ],
        animate=options.get("animate", False),
    )


def generate_matplotlib_chart_component(options: t.Options) -> t.Any:
    # fig = options.get("figure")
    # if fig is None:
    #     raise ValueError("'figure' is required for matplotlib charts.")
    # return MatplotlibChart(fig, expand=options.get("expand", False))
    raise NotImplementedError


def generate_pie_chart_component(options: t.Options) -> t.Any:
    sections = options.get("sections", [])
    pie_sections = [
        PieChartSection(
            value=s.get("value", 0),
            title=s.get("title"),
            color=s.get("color"),
            radius=s.get("radius"),
        ) for s in sections
    ]
    return PieChart(
        sections=pie_sections,
        center_space_radius=options.get("center_space_radius", 0),
    )


def generate_plotly_chart_component(options: t.Options) -> t.Any:
    # fig = options.get("figure")
    # if fig is None:
    #     raise ValueError("'figure' is required for Plotly charts.")
    # return PlotlyChart(fig, expand=options.get("expand", False))
    raise NotImplementedError