from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('datasets/dummies.csv')


tip_amount = df['tip_amount']


newData = df.drop(['tip_amount'], axis=1)



lr = linear_model.LinearRegression()



# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, newData, tip_amount, cv=10)

fig, ax = plt.subplots()
ax.scatter(tip_amount, predicted, edgecolors=(0, 0, 0))
ax.plot([tip_amount.min(), tip_amount.max()], [tip_amount.min(), tip_amount.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()