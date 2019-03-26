import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

dataset = pd.read_csv('datasets/dummies.csv')
datasetTarget = dataset['tip_amount']
labels = np.array(datasetTarget)
datasetFeatures = dataset.drop(['tip_amount'], axis=1)
feature_list = list(datasetFeatures.columns)
features = np.array(datasetFeatures)


train_x, test_x, train_y, test_y = train_test_split(datasetFeatures, datasetTarget,
                                                    test_size=0.2)

rf = RandomForestRegressor(n_estimators=100)
rf.fit(train_x, train_y)

predictions = rf.predict(test_x)
errors = abs(predictions-test_y)
print "Mean absolute error: ", round(np.mean(errors), 2)

mape = 100 * (errors/test_y)
accuracy = 100 - np.mean(mape)
print "Accuracy: ", round(accuracy, 2),"%"


