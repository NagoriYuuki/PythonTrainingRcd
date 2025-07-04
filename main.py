import json
from pyecharts import options as opts
from pyecharts.charts import Page, Bar, Pie, Line
from pyecharts.globals import ThemeType

theme = ThemeType.DARK

arr = ["vivo", "华为", "苹果", "OPPO", "荣耀", "其他"]
val_2024 = [49.3, 46.0, 42.9, 42.7, 42.2, 61.6]
val_2023 = [44.5, 33.5, 51.8, 43.9, 43.6, 55.3]
vivo = [71, 53.2, 44.5, 49.3]
diff = [11, 37, -17, -3, -3, 12]
share_pct = [17, 16, 15, 15, 15, 22]
market_share_data = [(arr[i], share_pct[i]) for i in range(len(arr))]


layout_config = [
    {"cid": "bar_2024_shipments", "top": "0%", "left": "0%", "width": "50%", "height": "50%"},
    {"cid": "bar_comparison", "top": "0%", "left": "50%", "width": "50%", "height": "50%"},
    {"cid": "pie_market_share", "top": "50%", "left": "0%", "width": "50%", "height": "50%"},
    {"cid": "bar_growth_rate", "top": "50%", "left": "50%", "width": "50%", "height": "50%"}
]

with open("chart_config.json", "w", encoding="utf-8") as f:
    json.dump(layout_config, f, ensure_ascii=False, indent=4)


bar1 = (
    Bar(init_opts=opts.InitOpts(theme=theme, chart_id="bar_2024_shipments"))
    .add_xaxis(arr)
    .add_yaxis("2024年出货量 (百万台)", val_2024)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="图1: 2024年主要厂商智能手机出货量", title_textstyle_opts=opts.TextStyleOpts(color="#fff")),
        xaxis_opts=opts.AxisOpts(name="厂商", axislabel_opts=opts.LabelOpts(color="#ccc")),
        yaxis_opts=opts.AxisOpts(name="出货量 (百万台)", axislabel_opts=opts.LabelOpts(color="#ccc")),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
)


line2 = (
    Line(init_opts=opts.InitOpts(theme=theme, chart_id="bar_comparison"))
    .add_xaxis(["2021", "2022", "2023", "2024"])
    .add_yaxis(
        "年出货量",
        vivo,
        is_smooth=True,
        is_symbol_show=True,
        symbol="circle",
        symbol_size=10
    )
    # .add_yaxis(
    #     series_name="2024年出货量",
    #     y_axis=val_2024,
    #     is_smooth=True,
    #     markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])
    # )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="图2: vivo手机年出货量趋势对比", title_textstyle_opts=opts.TextStyleOpts(color="#fff")
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="#fff")),
        xaxis_opts=opts.AxisOpts(name="年份", axislabel_opts=opts.LabelOpts(color="#ccc")),
        yaxis_opts=opts.AxisOpts(name="出货量 (百万台)", axislabel_opts=opts.LabelOpts(color="#ccc")),
    )
)

pie = (
    Pie(init_opts=opts.InitOpts(theme=theme, chart_id="pie_market_share"))
    .add(series_name="市场份额", data_pair=market_share_data, rosetype="radius", radius=["30%", "50%"])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="图3: 2024年市场份额", title_textstyle_opts=opts.TextStyleOpts(color="#fff")),legend_opts = opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="15%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
)

bar3 = (
    Bar(init_opts=opts.InitOpts(theme=theme, chart_id="bar_growth_rate"))
    .add_xaxis(arr)
    .add_yaxis("年增长率 (%)", diff)
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="图4: 主要厂商年度增长率", title_textstyle_opts=opts.TextStyleOpts(color="#fff")),
        xaxis_opts=opts.AxisOpts(name="增长率 (%)", axislabel_opts=opts.LabelOpts(color="#ccc")),
        yaxis_opts=opts.AxisOpts(name="厂商", axislabel_opts=opts.LabelOpts(color="#ccc")),
    )
    .set_series_opts(label_opts=opts.LabelOpts(position="right", formatter="{c}%"))
)

page = Page(page_title="2024手机市场分析大屏")
page.add(bar1, line2, pie, bar3)

page.render("temp.html")
Page.save_resize_html(
    source="temp.html",
    cfg_file="chart_config.json",
    dest="render.html"
)

print("Accepted")

