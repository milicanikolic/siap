import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
import numpy as np
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('datasets/dummies.csv')
datasetTarget = dataset['tip_amount']
datasetFeatures = dataset.drop(['tip_amount'], axis=1)

train_x, test_x, train_y, test_y = train_test_split(datasetFeatures, datasetTarget,
                                                    train_size=0.8)

model = linear_model.LinearRegression()
model.fit(train_x, train_y)

predictions = model.predict(test_x)


print('Coefficients: \n', model.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(test_y, predictions))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(test_y, predictions))

"""
# Plot outputs
plt.scatter(test_x, test_y,  color='black')
plt.plot(test_x, predictions, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())
plt.show()

"""

plt.scatter(test_y, predictions)
plt.xlabel(' REAL Tip Amount')
plt.ylabel(' PREDICTED Tip Amount')
plt.show()

