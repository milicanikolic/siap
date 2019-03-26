import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
import numpy as np

fields = ['boroughPickup_Bronx', 'boroughPickup_Brooklyn', 'boroughPickup_Queens', 'boroughPickup_Manhattan', 'boroughPickup_Staten Island',
          'tip_amount']

train = pd.read_csv('datasets/trainDummies.csv', skipinitialspace=True, usecols=fields)
test = pd.read_csv('datasets/testDummies.csv', skipinitialspace=True, usecols=fields)

tip_amountTRAIN = train['tip_amount']
tip_amountTEST = test['tip_amount']

newDataTRAIN = train.drop(['tip_amount'], axis=1)
newDataTEST = test.drop(['tip_amount'], axis=1)

model = linear_model.LinearRegression()
model.fit(newDataTRAIN, tip_amountTRAIN)

predictions = model.predict(newDataTEST)


print('Coefficients: \n', model.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(tip_amountTEST, predictions))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(tip_amountTEST, predictions))

print predictions.shape
print predictions
print tip_amountTEST



