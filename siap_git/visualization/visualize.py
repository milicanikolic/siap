import pandas as pd
import numpy as np
from bokeh.layouts import row
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from bokeh.io import output_file, show
from bokeh.models import (
    GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool
)

data = pd.read_csv('C:/Users/Milica/PycharmProjects/test/output/data.csv')

nyc_lat = 40.7127753
nyc_lon = -74.0059728

A_lat = 40.92984285194642
A_lon = -73.93167114270909
B_lat = 40.587572417681216
B_lon = -73.64046478061937
C_lat = 40.49641357209898
C_lon = -74.25288391532376

D_lat = 40.77073119523123
D_lon = -74.09069824847393

pickup_longitudes = data['pickup_longitude']
pickup_latitudes = data['pickup_latitude']
dropoff_longitudes = data['dropoff_longitude']
dropoff_latitudes = data['dropoff_latitude']

lons_vect = [A_lon, B_lon, C_lon]
lats_vect = [A_lat, B_lat, C_lat]
lons_lats_vect = np.column_stack((lons_vect, lats_vect))  # Reshape coordinates
polygon = Polygon(lons_lats_vect)  # create polygon

pickup_longitudes2 = []
pickup_latitudes2 = []
dropoff_longitudes2 = []
dropoff_latitudes2 = []

for lat, lon in zip(pickup_latitudes, pickup_longitudes):
    point = Point(lon, lat)
    if not polygon.contains(point):
        pickup_latitudes2.append(lat)
        pickup_longitudes2.append(lon)

for lat2, lon2 in zip(dropoff_latitudes, dropoff_longitudes):
    point = Point(lon2, lat2)
    if not polygon.contains(point):
        dropoff_latitudes2.append(lat2)
        dropoff_longitudes2.append(lon2)

map_options = GMapOptions(lat=40.7127753, lng=-74.0059728, map_type="roadmap", zoom=8)

plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot1 = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot.title.text = "NYC Pickups"
plot1.title.text = "NYC Dropoffs"

plot.api_key = "AIzaSyB_NaKqSwUSD_DDSkReMz9fycq96ph9VhE"

source = ColumnDataSource(
    data=dict(
        lat=pickup_latitudes2,
        lon=pickup_longitudes2,
    )
)
triangle = ColumnDataSource(
    data=dict(
        lat=lats_vect,
        lon=lons_vect,
    )
)
source2 = ColumnDataSource(
    data=dict(
        lat=dropoff_latitudes2,
        lon=dropoff_longitudes2,
    )
)

circle_triangle = Circle(x="lon", y="lat", size=10, fill_color="black", fill_alpha=0.8, line_color=None)
plot.add_glyph(triangle, circle_triangle)
plot1.add_glyph(triangle, circle_triangle)

circle = Circle(x="lon", y="lat", size=5, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

circle2 = Circle(x="lon", y="lat", size=5, fill_color="red", fill_alpha=0.8, line_color=None)
plot1.add_glyph(source2, circle2)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
plot1.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("pickUp_dropOff_modified_map.html")
show(row(plot, plot1))
