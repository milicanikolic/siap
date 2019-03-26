import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column,row
from bokeh.models import Range1d

fields = ['trip_distance','minutes', 'tip_amount','total_amount','passenger_count','days']
data = pd.read_csv('ds/filteredTrain1.csv', skipinitialspace=True, usecols=fields)

output_file('distance0.html')

data1=data[(data['trip_distance']==3)]


trip_distance=data1['trip_distance']
minutes=data1['minutes']
total_amount=data1['total_amount']
tip_amount=data1['tip_amount']

minutes_unique=minutes.unique()
minutes_count=data1['minutes'].value_counts()
count_per_minutes=minutes_count[minutes_unique]
print count_per_minutes

p=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=700,plot_height=300)
p.xgrid.grid_line_color=None
p.ygrid.grid_line_color=None
p.yaxis.axis_label="minutes count"
p.xaxis.axis_label="minutes"
p.vbar(x=minutes_unique, top=count_per_minutes, width=0.4, color='cyan')

trip_distance_u=trip_distance.unique()
trip_distance_c=trip_distance.value_counts()
count_per_trip_distance=trip_distance_c[trip_distance_u]

p2=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=700,plot_height=300)
p2.xgrid.grid_line_color=None
p2.ygrid.grid_line_color=None
p2.yaxis.axis_label="trip distances when minutes are < 3"
p2.xaxis.axis_label="count"
p2.vbar(x=trip_distance_u, top=count_per_trip_distance, width=0.4, color='blue')

p3=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=700,plot_height=300)
p3.xgrid.grid_line_color=None
p3.ygrid.grid_line_color=None
p3.yaxis.axis_label="trip distances when minutes are < 3"
p3.xaxis.axis_label="count"
p3.x_range=Range1d(-0.2,2)
p3.vbar(x=trip_distance_u, top=count_per_trip_distance, width=0.4, color='blue')

tip_amount_u=tip_amount.unique()
tip_amount_c=tip_amount.value_counts()
count_per_tip=tip_amount_c[tip_amount_u]

p4=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=700,plot_height=300)
p4.xgrid.grid_line_color=None
p4.ygrid.grid_line_color=None
p4.yaxis.axis_label="tips when minutes are < 3"
p4.xaxis.axis_label="count"
p4.vbar(x=tip_amount_u, top=count_per_tip, width=0.4, color='purple')

p5=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=700,plot_height=300)
p5.xgrid.grid_line_color=None
p5.ygrid.grid_line_color=None
p5.yaxis.axis_label="tips when minutes are < 3"
p5.xaxis.axis_label="count"
p5.x_range=Range1d(-0.2,5)
p5.vbar(x=tip_amount_u, top=count_per_tip, width=0.4, color='purple')

total_amount_u=total_amount.unique()
total_amount_c=total_amount.value_counts()
count_per_total=total_amount_c[total_amount_u]

p6=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=700,plot_height=300)
p6.xgrid.grid_line_color=None
p6.ygrid.grid_line_color=None
p6.yaxis.axis_label="total amount when minutes are < 3"
p6.xaxis.axis_label="count"
p6.vbar(x=total_amount_u, top=count_per_total, width=0.4, color='red')


p7=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=700,plot_height=300)
p7.xgrid.grid_line_color=None
p7.ygrid.grid_line_color=None
p7.yaxis.axis_label="total amount when minutes are < 3"
p7.xaxis.axis_label="count"
p7.x_range=Range1d(-0.1,10)
p7.vbar(x=total_amount_u, top=count_per_total, width=0.4, color='red')

show(column(p,row(p2,p3),row(p4,p5),row(p6,p7)))