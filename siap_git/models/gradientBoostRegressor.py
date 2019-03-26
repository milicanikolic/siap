import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import ShuffleSplit, train_test_split


df = pd.read_csv('datasets/dummies.csv')
target = df['tip_amount']
features = df.drop(['tip_amount'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(features, target, train_size=0.8)
gbrt=GradientBoostingRegressor(n_estimators=100)
gbrt.fit(X_train, y_train)
y_pred=gbrt.predict(X_test)


print "Feature Importances"
print gbrt.feature_importances_
print
#Let's print the R-squared value for train/test. This explains how much of the variance in the data our model is #able to decipher.
print "R-squared for Train: %.2f" %gbrt.score(X_train, y_train)
print "R-squared for Test: %.2f" %gbrt.score(X_test, y_test)