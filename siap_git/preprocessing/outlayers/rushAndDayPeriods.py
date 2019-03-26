import pandas as pd
import sqlalchemy
import collections
from sqlalchemy import create_engine
import numpy as np
from datetime import datetime
import datetime as dtt
import matplotlib.pyplot as plt

database = create_engine('sqlite:///database.db')

fields = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'payment_type', 'passenger_count', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'RatecodeID', 'dropoff_longitude', 'dropoff_latitude',
        'payment_type', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount']
df = pd.read_csv('dataset/yellow_tripdata_2016-01.csv', skipinitialspace=True, usecols=fields)
df = df[(df['payment_type'] == 1)]
df = df.drop('payment_type', 1)

#print df

pickUpDate = pd.to_datetime(df['tpep_pickup_datetime'])
dropOffDate = pd.to_datetime(df['tpep_dropoff_datetime'])
df.loc[:, 'tpep_pickup_datetime'] = pickUpDate
df.loc[:, 'tpep_dropoff_datetime'] = dropOffDate

df.to_sql('dayPeriods', database, if_exists='replace', dtype={'tpep_pickup_datetime': sqlalchemy.DateTime(),'tpep_dropoff_datetime' :sqlalchemy.DateTime()})

"""df = pd.read_sql_query("SELECT * FROM 'dayPeriods'", database, parse_dates={'tpep_pickup_datetime', 'tpep_dropoff_datetime'})

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

trip_duration = df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']
outlayers = trip_duration[(trip_duration.dt.days == 1) | (trip_duration.dt.components.hours > (dtt.timedelta(hours = 5).seconds)/3600)]

df.to_csv('dataset/dataPeriodsAndRush.csv', index = False)


hours = pd.to_datetime(outlayers).dt.hour
print hours.value_counts() """
