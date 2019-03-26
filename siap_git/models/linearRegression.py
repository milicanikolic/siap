import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
import numpy as np

train = pd.read_csv('datasets/trainDummies.csv')
test = pd.read_csv('datasets/testDummies.csv')

tip_amountTRAIN = train['tip_amount']
tip_amountTEST = test['tip_amount']

newDataTRAIN = train.drop(['tip_amount', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'], axis=1)
newDataTEST = test.drop(['tip_amount', 'tpep_pickup_datetime', 'tpep_dropoff_datetime'], axis=1)

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


# Plot outputs
plt.scatter(newDataTEST, tip_amountTEST,  color='black')
plt.plot(newDataTEST, predictions, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

