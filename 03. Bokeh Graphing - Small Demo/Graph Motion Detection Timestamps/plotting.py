from motion_detector import df
import pandas
from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type = "datetime", height =500, width = 1000, title ="Motion Graph", sizing_mode="scale_width" )

q = p.quad(left = df["Start"], right = df["End"], bottom = 0, top = 1, color = "green")

output_file("TimeDetectionGraph.html")
show(p)