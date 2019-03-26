#vizializavija koordinata pocetka i kraja voznje na malom delu dataseta
import pandas as pd
from bokeh.layouts import row
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool
)

data = pd.read_csv('C:/Users/Milica/PycharmProjects/test/dataset/subset2.csv')

nyc_lat=40.7127753
nyc_lon=-74.0059728

map_options = GMapOptions(lat=nyc_lat, lng=nyc_lon, map_type="roadmap", zoom=9)

plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot1 = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot.title.text = "NYC Pickups"
plot1.title.text = "NYC Dropoff"

plot.api_key = "AIzaSyB_NaKqSwUSD_DDSkReMz9fycq96ph9VhE"
plot1.api_key = "AIzaSyB_NaKqSwUSD_DDSkReMz9fycq96ph9VhE"

pickup_longitudes=data['pickup_longitude']
pickup_latitudes=data['pickup_latitude']
dropoff_longitudes=data['dropoff_longitude']
dropoff_latitudes=data['dropoff_latitude']

source1 = ColumnDataSource(
    data=dict(
        lat=pickup_latitudes,
        lon=pickup_longitudes,
    )
)

source2 = ColumnDataSource(
    data=dict(
        lat=dropoff_latitudes,
        lon=dropoff_longitudes,
    )
)
circle = Circle(x="lon", y="lat", size=8, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source1, circle)
circle2 = Circle(x="lon", y="lat", size=8, fill_color="red", fill_alpha=0.8, line_color=None)
plot1.add_glyph(source2, circle2)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
plot1.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("pickUp_dropOff_map.html")
show(row(plot,plot1))