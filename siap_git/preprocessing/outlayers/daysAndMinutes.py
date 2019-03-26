import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import datetime as dtt


fields = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'payment_type', 'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'RatecodeID', 'dropoff_longitude', 'dropoff_latitude',
        'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount']
df = pd.read_csv('dataset/originalTrain.csv', skipinitialspace=True, usecols=fields)
df = df[(df['payment_type'] == 1)]
df = df.drop('payment_type', 1)

pickUpDate = pd.to_datetime(df['tpep_pickup_datetime'])
dropOffDate = pd.to_datetime(df['tpep_dropoff_datetime'])
df.loc[:, 'tpep_pickup_datetime'] = pickUpDate
df.loc[:, 'tpep_dropoff_datetime'] = dropOffDate

df['days'] = df['tpep_pickup_datetime'].dt.weekday

df['index'] = df.index
#outlayers = df[((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.days > 0) | ((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']) <= pd.Timedelta('0 days 00:00:00'))]
outlayers = df[((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.days > 0)]
print outlayers
df = df.append(outlayers).drop_duplicates(keep=False)
df = df.drop('index', 1)





df['minutes'] = ((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds())/60 % 60


df.to_csv('dataset/dataDays.csv', index = False)
