import pandas as pd
from pyecharts.charts import *
import pyecharts.options as opts
import ast
from io import StringIO

from pyecharts.globals import ThemeType

# csv_data = """date,title,rating_or_passnum,pass_rate,tags
# "July 1, 2025",Blackboard Game,513.0,99.78,['math']
# "July 1, 2025",Tournament,768.0,99.06,['greedy']
# "July 1, 2025",Prefix Min and Suffix Max,905.0,97.95,"['brute force', 'data structures']"
# "July 1, 2025",Binary String Battle,1259.0,86.18,"['constructive algorithms', 'games', 'greedy']"
# "July 1, 2025",MEX Count,1470.0,64.93,"['binary search', 'data structures', 'greedy', 'sortings', 'two pointers']"
# "July 1, 2025",Minimize Fixed Points,1702.0,32.75,"['constructive algorithms', 'number theory']"
# "July 1, 2025",Modular Sorting,2203.0,2.65,"['brute force', 'data structures', 'greedy', 'math', 'number theory']"
# """

df = pd.read_csv("cf_cleaned.csv", encoding="utf-8-sig")
# df = pd.read_csv(StringIO(csv_data))

def safe_parse_tags(tag_string):

    if not isinstance(tag_string, str):
        return []
    try:
        return ast.literal_eval(tag_string)
    except (ValueError, SyntaxError):
        return []


df['tags_list'] = df['tags'].apply(safe_parse_tags)
all_tags = df['tags_list'].explode()
tag_counts = all_tags.value_counts().head(30)

theme = ThemeType.DARK
if not tag_counts.empty:

    y_axis_data = [int(v) for v in tag_counts.values]

    bar = (
        Bar(init_opts=opts.InitOpts(width="100%", height="600px",theme=theme,chart_id="top10algorithms"))
        .add_xaxis(list(tag_counts.index))
        # 使用转换后的 y_axis_data
        .add_yaxis("出现次数", y_axis_data, color="#5470C6")
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Codeforces 热门算法标签 Top 30",
                subtitle="根据题目出现频率统计",
                pos_left="center"
            ),
            xaxis_opts=opts.AxisOpts(
                name="标签",
                axislabel_opts=opts.LabelOpts(rotate=30, font_size=12)  # 旋转标签防止重叠
            ),
            yaxis_opts=opts.AxisOpts(name="出现次数"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="shadow"),
            legend_opts=opts.LegendOpts(is_show=False)
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最高频率"),
                    opts.MarkPointItem(type_="min", name="最低频率"),
                ]
            ),
        )
    )

    page=Page().add(bar).render("tempcf.html")
    # page.add(bar)
    Page.save_resize_html(
        source="tempcf.html",
        cfg_file="cfcharts.json",
        dest="rendered_cfcharts.html"
    )
    print("Accepted")

else:
    print("错误：未能从数据中提取任何标签。请检查 'tags' 列的格式是否正确。")
