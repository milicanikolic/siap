import pandas as pd
import collections
import matplotlib.pyplot as plt


fields = ['tpep_pickup_datetime', 'tpep_dropoff_datetime', 'payment_type']
frame = pd.read_csv('C:/Users/Milica/PycharmProjects/test/dataset/yellow_tripdata_2016-01.csv', skipinitialspace=True, usecols=fields)

frame = frame.loc[frame['payment_type'] == 1]

pickUpDate = pd.to_datetime(frame.tpep_pickup_datetime)
dropOffDate = pd.to_datetime(frame.tpep_dropoff_datetime)

sub = dropOffDate-pickUpDate
durationInMin = sub.astype('timedelta64[m]')
durInt = durationInMin.astype(int)

durInt.hist(bins=durationInMin.size)
plt.xticks(durationInMin.astype(int))
counter = collections.Counter(sub)
plt.yticks(counter.values())
plt.show()





