import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np

df=pd.read_csv('datasets/filteredTest.csv')
print df.shape

A_lat = 40.92984285194642
A_lon = -73.93167114270909
B_lat = 40.587572417681216
B_lon = -73.64046478061937
C_lat = 40.49641357209898
C_lon = -74.25288391532376

lons_vect = [A_lon, B_lon, C_lon]
lats_vect = [A_lat, B_lat, C_lat]
lons_lats_vect = np.column_stack((lons_vect, lats_vect))  # Reshape coordinates
polygon = Polygon(lons_lats_vect)  # create polygon

brojac=0
deleteIndexes=[]

df['id']=df.index
indexes=df.id
pickup_latitudes=df.pickup_latitude
pickup_longitudes=df.pickup_longitude
dropoff_latitudes=df.dropoff_latitude
dropoff_longitudes=df.dropoff_longitude

for latP, lonP, latD, lonD, inx in zip(pickup_latitudes, pickup_longitudes, dropoff_latitudes, dropoff_longitudes,indexes):
    pointP = Point(lonP, latP)
    pointD = Point(lonD, latD)
    brojac=brojac+1
    if not(polygon.contains(pointP) & polygon.contains(pointD)):
        deleteIndexes.append(inx)
    if(brojac==10000):
        print brojac
        brojac=0



deleteID=pd.DataFrame(deleteIndexes, columns=['ID'])
indexes = np.asarray(deleteID.as_matrix()).reshape(-1)
indexes=indexes.tolist()
df = df.loc[~df['id'].isin(indexes)]

df=df.drop('id',1)
df.to_csv('datasets/filteredTest.csv', index = False)
print df.shape
