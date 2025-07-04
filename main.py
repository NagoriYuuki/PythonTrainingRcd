from pyecharts import options as opts
from pyecharts.charts import *

arr = ["vivo", "华为", "苹果", "OPPO", "荣耀", "其他"]
val = [49.3, 46.0, 42.9, 42.7, 42.2, 61.6]
mp = [
    ("vivo", 17),
    ("华为", 16),
    ("苹果", 15),
    ("OPPO", 15),
    ("荣耀", 15),
    ("其他", 22),
]
val2 = [44.5, 33.5, 51.8, 43.9, 43.6, 55.3]
diff = [11, 37, -17, -3, -3, 12]

# print(*mp)

bar = Bar().add_xaxis(arr).add_yaxis("2024年出货量 (百万台)", val).set_global_opts(
    title_opts=opts.TitleOpts(title="图1: 2024年主要厂商智能手机出货量"),
    yaxis_opts=opts.AxisOpts(name="出货量 (百万台)"),
    xaxis_opts=opts.AxisOpts(name="厂商"),
).set_series_opts(label_opts=opts.LabelOpts(is_show=True))

pie = Pie().add(
    series_name="市场份额",
    data_pair=mp,
    rosetype="radius",
).set_global_opts(
    title_opts=opts.TitleOpts(title="图2: 2024年中国大陆智能手机市场份额"),
    legend_opts = opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
).set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))

line = Line().add_xaxis(arr).add_yaxis("2023年出货量", val2).add_yaxis("2024年出货量", val).set_global_opts(
    title_opts=opts.TitleOpts(title="图3: 2023 vs 2024 主要厂商出货量对比"),
    yaxis_opts=opts.AxisOpts(name="出货量 (百万台)"),
    xaxis_opts=opts.AxisOpts(name="厂商"),
    tooltip_opts=opts.TooltipOpts(trigger="axis"),
)
growth = Bar().add_xaxis(arr).add_yaxis("年增长率 (%)", diff).reversal_axis().set_global_opts(
    title_opts=opts.TitleOpts(title="图4: 主要厂商年度增长率对比"),
    xaxis_opts=opts.AxisOpts(name="增长率 (%)"),
    yaxis_opts=opts.AxisOpts(name="厂商"),
).set_series_opts(label_opts=opts.LabelOpts(position="right", formatter="{c}%"))

page = Page(layout=Page.SimplePageLayout).add(
    bar,
    pie,
    line,
    growth,
).render("test.html")
