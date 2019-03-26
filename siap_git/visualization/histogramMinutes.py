import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column,row
from bokeh.models import Range1d

data = pd.read_csv('datasets/filteredV1.csv')

output_file('histogram_minutesV1filtered.html')

minutes=data['minutes'].unique()
minutes_count=data['minutes'].value_counts()
count_per_minutes=minutes_count[minutes]

minutesF = figure(plot_height=700, plot_width=1000, title="Minutes of trip duration")
minutesF.vbar(x=minutes, top=count_per_minutes, width=0.9, color='red')
minutesF.xgrid.grid_line_color = None

minutesF2 = figure(plot_height=700, plot_width=1000, title="Minutes of trip duration")
minutesF2.vbar(x=minutes, top=count_per_minutes, width=0.9, color='red')
minutesF2.xgrid.grid_line_color = None
minutesF2.x_range=Range1d(-3,100)

minutesF3 = figure(plot_height=700, plot_width=1000, title="Minutes of trip duration")
minutesF3.vbar(x=minutes, top=count_per_minutes, width=0.9, color='red')
minutesF3.xgrid.grid_line_color = None
minutesF3.x_range=Range1d(40,83)
minutesF3.y_range=Range1d(0,1000)

minutesF4 = figure(plot_height=700, plot_width=1000, title="Minutes of trip duration")
minutesF4.vbar(x=minutes, top=count_per_minutes, width=0.9, color='red')
minutesF4.xgrid.grid_line_color = None
minutesF4.x_range=Range1d(1250,1460)
minutesF4.y_range=Range1d(0,1000)

show(column(minutesF,minutesF2,minutesF3,minutesF4))
