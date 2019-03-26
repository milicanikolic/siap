import pandas as pd
from datetime import datetime
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

fields = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'payment_type', 'passenger_count', 'trip_distance', 'pickup_longitude',
          'pickup_latitude', 'RatecodeID', 'dropoff_longitude', 'dropoff_latitude', 'tip_amount', 'total_amount']
df = pd.read_csv('datasets/original.csv', skipinitialspace=True, usecols=fields)
df = df[(df['payment_type'] == 1)]
df = df.drop('payment_type', 1)

pickUpDate = pd.to_datetime(df['tpep_pickup_datetime'])
dropOffDate = pd.to_datetime(df['tpep_dropoff_datetime'])
df.loc[:, 'tpep_pickup_datetime'] = pickUpDate
df.loc[:, 'tpep_dropoff_datetime'] = dropOffDate

df['trip_amount'] = df.total_amount - df.tip_amount
df = df.drop('total_amount', 1)

df = df[(df['trip_amount'] >= 3) & (df['trip_amount'] <= 500)]
df = df[(df['tip_amount'] >= 0) & (df['tip_amount'] < 200)]
df = df[(df['passenger_count'] > 0) & (df['passenger_count'] < 7)]
df = df[(df['RatecodeID'] == 1) | (df['RatecodeID'] == 2) | (df['RatecodeID'] == 3) | (df['RatecodeID'] == 4) | (df['RatecodeID'] == 5)| (df['RatecodeID'] == 6)]
df = df[(df['RatecodeID'] == 1) | (df['RatecodeID'] == 2) | (df['RatecodeID'] == 5)]

df = df.drop(df.index[df['trip_distance'].idxmax()])
df = df[(df['trip_distance'] >= 1) & (df['trip_distance'] <= 65)]

df['id'] = df.index
outlayers = df[((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.days > 0)]
df = df.append(outlayers).drop_duplicates(keep=False)

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

deleteIndexes=[]

indexes=df.id
pickup_latitudes=df.pickup_latitude
pickup_longitudes=df.pickup_longitude
dropoff_latitudes=df.dropoff_latitude
dropoff_longitudes=df.dropoff_longitude

for latP, lonP, latD, lonD, inx in zip(pickup_latitudes, pickup_longitudes, dropoff_latitudes, dropoff_longitudes,indexes):
    pointP = Point(lonP, latP)
    pointD = Point(lonD, latD)
    if not(polygon.contains(pointP) & polygon.contains(pointD)):
        deleteIndexes.append(inx)

deleteID=pd.DataFrame(deleteIndexes, columns=['ID'])
indexes = np.asarray(deleteID.as_matrix()).reshape(-1)
indexes=indexes.tolist()
df = df.loc[~df['id'].isin(indexes)]

rushMorningStart = datetime.time(pd.to_datetime('07:00:00'))
rushMorningEnd = datetime.time(pd.to_datetime('09:00:00'))
rushEveningStart = datetime.time(pd.to_datetime('18:00:00'))
rushEveningEnd = datetime.time(pd.to_datetime('20:00:00'))

df['rushHour'] = np.nan
df['rushHour'] = (((df['tpep_pickup_datetime'].dt.time >= rushMorningStart) & (df['tpep_pickup_datetime'].dt.time <= rushMorningEnd)) | ((df['tpep_pickup_datetime'].dt.time >= rushEveningStart) & (df['tpep_pickup_datetime'].dt.time <= rushEveningEnd))).astype(int)

conditions = [
    (df['tpep_pickup_datetime'].dt.time >= datetime.time(pd.to_datetime('05:00:00'))) & (df['tpep_pickup_datetime'].dt.time < datetime.time(pd.to_datetime('12:00:00'))),
    (df['tpep_pickup_datetime'].dt.time >= datetime.time(pd.to_datetime('12:00:00'))) & (df['tpep_pickup_datetime'].dt.time < datetime.time(pd.to_datetime('17:00:00'))),
    (df['tpep_pickup_datetime'].dt.time >= datetime.time(pd.to_datetime('17:00:00'))) & (df['tpep_pickup_datetime'].dt.time < datetime.time(pd.to_datetime('21:00:00'))),
    (df['tpep_pickup_datetime'].dt.time >= datetime.time(pd.to_datetime('21:00:00'))) | (df['tpep_pickup_datetime'].dt.time < datetime.time(pd.to_datetime('05:00:00')))
    ]
choices = ['morning', 'afternoon', 'evening', 'night']
df['periodOfDay'] = np.select(conditions, choices, default=np.nan)

df['minutes'] = np.round((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds()/60).astype(int)
df = df[(df['minutes'] >= 3) & (df['minutes'] < 80)]

df['days'] = df['tpep_pickup_datetime'].dt.weekday



df = df.drop('id', 1)

df.loc[:, 'tpep_pickup_datetime'] = df['tpep_pickup_datetime'].dt.time
df.loc[:, 'tpep_dropoff_datetime'] = df['tpep_dropoff_datetime'].dt.time

df.to_csv('datasets/filteredV1.csv', index = False)