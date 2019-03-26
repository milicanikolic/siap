import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

data = pd.read_csv('C:/Users/Milica/PycharmProjects/test/output/data.csv')
#data = pd.read_csv('C:/Users/Milica/PycharmProjects/test/dataset/subset2.csv')

count=data['days'].value_counts()
days=data['days'].unique()
count_per_day=count[days]

output_file('bar.html')

daysF = figure(x_range=days, plot_height=500, plot_width=1000, title="Days",
           toolbar_location=None, tools="")
daysF.vbar(x=days, top=count_per_day, width=0.9, color='pink')
daysF.xgrid.grid_line_color = None
daysF.y_range.start = 0


minutes=data['minutes'].unique()
minutes_count=data['minutes'].value_counts()
count_per_minutes=minutes_count[minutes]

minutesF = figure(plot_height=500, plot_width=1000, title="Minutes of trip")
minutesF.vbar(x=minutes, top=count_per_minutes, width=0.9, color='black')
minutesF.xgrid.grid_line_color = None


print 'Min minute: ', minutes.min(),' , Max minute: ',minutes.max()

distances=data['trip_distance'].unique()
distances_count=data['trip_distance'].value_counts()
count_per_distance=distances_count[distances]

distanceF = figure(plot_height=500, plot_width=1000, title="Distance of trip")
distanceF.vbar(x=distances, top=count_per_distance, width=0.9, color='red')
distanceF.xgrid.grid_line_color = None

print 'Min distance: ', distances.min(),' , Max distance: ',distances.max()


tip_amounts=data['tip_amount'].unique()
tip_amounts_count=data['tip_amount'].value_counts()
count_per_tip_amount=tip_amounts_count[tip_amounts]

tip_amountF = figure(plot_height=500, plot_width=1000, title="Tip amount")
#tip_amountF.vbar(x=tip_amounts, top=count_per_tip_amount, width=0.9, color='yellow')
tip_amountF.circle(tip_amounts, count_per_tip_amount, size=8, color="navy", alpha=0.5)
tip_amountF.xgrid.grid_line_color = None

print 'Min tip amount: ', tip_amounts.min(),' , Max tip amount: ',tip_amounts.max()

minutes_all=data['minutes']
distances_all=data['trip_distance']

minute_distance=figure(plot_height=500, plot_width=1000, title="Minutes-distance")
minute_distance.circle(minutes_all, distances_all, size=8, color="navy", alpha=0.5)
minute_distance.xaxis[0].axis_label = 'Minutes'
minute_distance.yaxis[0].axis_label = 'Distance (miles)'
minute_distance.xgrid.grid_line_color = None

#show(daysF)
#show(minutesF)
#show(distanceF)
show(tip_amountF)
#show(minute_distance)



