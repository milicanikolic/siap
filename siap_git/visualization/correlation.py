import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column,row
from bokeh.models import Range1d
import datashader as ds
from datashader.bokeh_ext import InteractiveImage

fields = ['trip_distance','minutes', 'tip_amount','total_amount','passenger_count','days']
data = pd.read_csv('ds/filteredTrain1.csv', skipinitialspace=True, usecols=fields)

output_file('correlation.html')

data1=data[(data['trip_distance']==0)]

trip_distance=data1['trip_distance']
minutes=data1['minutes']
total_amount=data1['total_amount']
tip_amount=data1['tip_amount']

p=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=1000,plot_height=700)
p.xgrid.grid_line_color=None
p.ygrid.grid_line_color=None
p.xaxis.axis_label="distance(miles)"
p.yaxis.axis_label="minutes"
p.circle(x=trip_distance, y=minutes, size=5,color='black')


p2=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=1000,plot_height=700)
p2.xgrid.grid_line_color=None
p2.ygrid.grid_line_color=None
p2.xaxis.axis_label="distance(miles)"
p2.yaxis.axis_label="total amount"
p2.circle(x=trip_distance, y=total_amount, size=5,color='green')

p3=figure(tools='pan,wheel_zoom,box_zoom,reset',plot_width=1000,plot_height=700)
p3.xgrid.grid_line_color=None
p3.ygrid.grid_line_color=None
p3.xaxis.axis_label="distance(miles)"
p3.yaxis.axis_label="tip amount"
p3.circle(x=trip_distance, y=tip_amount, size=5,color='red')
'''''
data2=data[(data['minutes']>3)&(data['minutes']<10)]
minutes2=data2['minutes']
trip_distance2=data2['trip_distance']

p2=figure(x_range=(2.5,10),tools='pan,wheel_zoom,box_zoom,reset',plot_width=800,plot_height=500)
p2.xgrid.grid_line_color=None
p2.ygrid.grid_line_color=None
p2.xaxis.axis_label="minutes of trip"
p2.yaxis.axis_label="distance(miles)"

p2.circle(x=minutes2, y=trip_distance2, size=5,color='black')
'''


show(column(p,p2,p3))


'''''
brojac=0
d=[]
t=[]

for i,j in zip(trip_distance,tip_amount):
    d.append(i)
    t.append(j)
    brojac=brojac+1
    if brojac==100000:
        break


distance_tipF = figure(plot_width=1000, plot_height=600)
distance_tipF.circle(d, t, size=4, color="navy", alpha=0.8)
distance_tipF.xaxis[0].axis_label='Trip distance(miles)'
distance_tipF.yaxis[0].axis_label='Tip amount($)'

distance_tipF2 = figure(plot_width=1000, plot_height=600)
distance_tipF2.circle(d, t, size=4, color="navy", alpha=0.8)
distance_tipF2.x_range=Range1d(-1,50)
distance_tipF2.y_range=Range1d(0,100)
distance_tipF2.xaxis[0].axis_label='Trip distance(miles)'
distance_tipF2.yaxis[0].axis_label='Tip amount($)'

distance_tipF3 = figure(plot_width=1000, plot_height=600)
distance_tipF3.circle(d, t, size=4, color="navy", alpha=0.8)
distance_tipF3.x_range=Range1d(-1,10)
distance_tipF3.y_range=Range1d(0,100)
distance_tipF3.xaxis[0].axis_label='Trip distance(miles)'
distance_tipF3.yaxis[0].axis_label='Tip amount($)'

show(column(distance_tipF,distance_tipF2,distance_tipF3))
'''