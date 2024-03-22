from bokeh.plotting import figure, show, output_file
from bokeh.models import Legend, LegendItem

p = figure(title="Line Graph with Annotations and Legends", x_axis_label="X-axis", y_axis_label="Y-axis")

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 1, 3, 6]
y2 = [1, 3, 2, 4, 5]

line1 = p.line(x, y1, line_width=2, legend_label="Line 1", line_color="blue")
line2 = p.line(x, y2, line_width=2, legend_label="Line 2", line_color="green")

p.circle(3, 1, size=10, fill_color="red", legend_label="Annotation")
p.text(2.5, 0.5, text=["Important Point"], text_font_size="10pt", text_color="red")

legend = Legend(items=[
    LegendItem(label="Line 1", renderers=[line1]),
    LegendItem(label="Line 2", renderers=[line2]),
    LegendItem(label="Annotation", renderers=[p.renderers[2]]),
])
p.add_layout(legend)

output_file("line_graph_with_annotations_and_legends.html")

show(p)


# ***** 8b 🫠 *****

# from bokeh.plotting import figure, output_file, show
# from bokeh.io import export_png
# from bokeh.layouts import row, column
# from bokeh.models import ColumnDataSource, HoverTool
# import numpy as np

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# output_file("bokeh_plots.html")

# line_plot = figure(title="Line Plot", x_axis_label="X-axis", y_axis_label="Y-axis")
# line_plot.line(x, y, line_width=2, legend_label="sin(x)", line_color="blue")

# scatter_plot = figure(title="Scatter Plot", x_axis_label="X-axis", y_axis_label="Y-axis")
# scatter_plot.scatter(x, y, marker="circle", size=8, color="red", legend_label="Data Points")

# categories = ["Category A", "Category B", "Category C", "Category D"]
# values = [30, 45, 60, 25]
# bar_chart = figure(x_range=categories, title="Bar Chart", x_axis_label="Categories", y_axis_label="Values")
# bar_chart.vbar(x=categories, top=values, width=0.5, color="green", legend_label="Values")

# hist_data = np.random.normal(0, 1, 1000)
# hist = figure(title="Histogram", x_axis_label="Value", y_axis_label="Frequency")
# hist.quad(top=np.histogram(hist_data, bins=30)[0], bottom=0, left=np.histogram(hist_data, bins=30)[1][:-1], right=np.histogram(hist_data, bins=30)[1][1:], fill_color="blue")

# scatter_source = ColumnDataSource(data=dict(x=x, y=y))
# hover = HoverTool()
# hover.tooltips = [("X", "@x"), ("Y", "@y")]
# scatter_plot.add_tools(hover)

# layout = column(
#     row(line_plot, scatter_plot),
#     row(bar_chart, hist)
# )

# show(layout)
# export_png(layout, filename="bokeh_plots.png")
