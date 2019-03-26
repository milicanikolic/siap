import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column,row
from bokeh.models import Range1d
import numpy as np
from scipy import stats

data = pd.read_csv('datasets/filteredV1.csv')

output_file('histogramsV1filtered.html')

count=data['days'].value_counts()
days=data['days'].unique()
count_per_day=count[days]

d=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
daysF = figure(x_range=d, plot_height=500, plot_width=1000, title="Days",
           toolbar_location=None, tools="")
daysF.vbar(x=days, top=count_per_day, width=0.9, color='pink')
daysF.xgrid.grid_line_color = None
daysF.y_range.start = 0


distances=data['trip_distance'].unique()
distances_count=data['trip_distance'].value_counts()
count_per_distance=distances_count[distances]

distanceF = figure(plot_height=500, plot_width=700, title="Distance of trip")
distanceF.vbar(x=distances, top=count_per_distance, width=0.9, color='red')
distanceF.xgrid.grid_line_color = None

distanceF2 = figure(plot_height=500, plot_width=700, title="Distance of trip")
distanceF2.vbar(x=distances, top=count_per_distance, width=0.5, color='red')
distanceF2.xgrid.grid_line_color = None
distanceF2.x_range = Range1d(30, 65)
distanceF2.y_range = Range1d(0, 30)
print 'Min distance: ', distances.min(),' , Max distance: ',distances.max()


passenger=data['passenger_count'].unique()
passenger_c=data['passenger_count'].value_counts()
count_per_passenger=passenger_c[passenger]

passengerF = figure(plot_height=500, plot_width=1000, title="Passengers count")
passengerF.vbar(x=passenger, top=count_per_passenger, width=0.9, color='green')
passengerF.xgrid.grid_line_color = None

print 'Min passenger count: ', passenger.min(),' , Max passenger count: ',passenger.max()


tip_amounts=data['tip_amount'].unique()
tip_amounts_count=data['tip_amount'].value_counts()
count_per_tip_amount=tip_amounts_count[tip_amounts]

tip_amountF = figure(plot_height=500, plot_width=700, title="Tip amount")
tip_amountF.vbar(x=tip_amounts, top=count_per_tip_amount, width=0.4, color='brown')
tip_amountF4 = figure(plot_height=500, plot_width=700, title="Tip amount")
tip_amountF4.vbar(x=tip_amounts, top=count_per_tip_amount, width=0.4, color='brown')
tip_amountF4.x_range=Range1d(0,100)
tip_amountF4.y_range=Range1d(0,20000)
tip_amountF2 = figure(plot_height=500, plot_width=700, title="Tip amount")
tip_amountF2.vbar(x=tip_amounts, top=count_per_tip_amount, width=0.4, color='brown')
tip_amountF2.x_range=Range1d(600,1000)
tip_amountF2.y_range=Range1d(0,20)

tip_amountF3 = figure(plot_height=500, plot_width=700, title="Tip amount")
tip_amountF3.vbar(x=tip_amounts, top=count_per_tip_amount, width=0.4, color='brown')
tip_amountF3.x_range=Range1d(200,600)
tip_amountF3.y_range=Range1d(0,30)
#tip_amountF.circle(tip_amounts, count_per_tip_amount, size=8, color="navy", alpha=0.5)
tip_amountF.xgrid.grid_line_color = None

print 'Min tip amount: ', tip_amounts.min(),' , Max tip amount: ',tip_amounts.max()


total_amount=data['trip_amount'].unique()
total_amount_count=data['trip_amount'].value_counts()
count_per_total_amount=total_amount_count[total_amount]

total_amountF = figure(plot_height=500, plot_width=700, title="Trip amount")
total_amountF.vbar(x=total_amount, top=count_per_total_amount, width=0.4, color='cyan')
total_amountF.y_range=Range1d(0,1000)
total_amountF2 = figure(plot_height=500, plot_width=700, title="Trip amount")
total_amountF2.vbar(x=total_amount, top=count_per_total_amount, width=0.4, color='cyan')
total_amountF3 = figure(plot_height=500, plot_width=700, title="Trip amount")
total_amountF3.vbar(x=total_amount, top=count_per_total_amount, width=0.4, color='cyan')
total_amountF3.x_range=Range1d(0,10)
total_amountF3.y_range=Range1d(0,500)
total_amountF4 = figure(plot_height=500, plot_width=700, title="Trip amount")
total_amountF4.vbar(x=total_amount, top=count_per_total_amount, width=0.4, color='cyan')
total_amountF4.x_range=Range1d(300,1000)
total_amountF4.y_range=Range1d(0,200)
print 'Min amount: ', total_amount.min(),' , Max amount: ',total_amount.max()

RatecodeID=data['RatecodeID'].unique()
RatecodeID_count=data['RatecodeID'].value_counts()
count_per_RatecodeID=RatecodeID_count[RatecodeID]

RatecodeIDF = figure(plot_height=500, plot_width=1000, title="RatecodeID")
RatecodeIDF.vbar(x=RatecodeID, top=count_per_RatecodeID, width=0.4, color='magenta')
RatecodeIDF.xgrid.grid_line_color = None


show(column(daysF,row(distanceF,distanceF2),passengerF,row(tip_amountF,tip_amountF4) ,row(tip_amountF2,tip_amountF3),row(total_amountF,total_amountF2),
row(total_amountF3, total_amountF4),RatecodeIDF))

