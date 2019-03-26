import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import numpy as np


train = pd.read_csv('datasets/trainDummies.csv')
test = pd.read_csv('datasets/testDummies.csv')

tip_amountTRAIN = train['tip_amount']
tip_amountTEST = test['tip_amount']

newDataTRAIN = train.drop(['tip_amount', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'minutes', 'trip_amount', 'trip_distance'], axis=1)
newDataTEST = test.drop(['tip_amount', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'minutes', 'trip_amount', 'trip_distance'], axis=1)

lm = LinearRegression()
lm.fit(newDataTRAIN, tip_amountTRAIN)

coef = pd.DataFrame(zip(newDataTRAIN.columns, lm.coef_), columns=['features', 'estimated coef'])
coef.to_csv('models/coefficients3.csv', index=False)

predicitons = lm.predict(newDataTRAIN)
plt.scatter(tip_amountTRAIN, predicitons)
plt.xlabel(' REAL Tip Amount')
plt.ylabel(' PREDICTED Tip Amount')
plt.show()