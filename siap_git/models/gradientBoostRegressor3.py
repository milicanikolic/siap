from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import ShuffleSplit, train_test_split
from sklearn.model_selection import GridSearchCV
import pandas as pd


df = pd.read_csv('datasets/dummies.csv')
target = df['tip_amount']
features = df.drop(['tip_amount'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, target, train_size=0.8)

estimator = GradientBoostingRegressor(n_estimators=100, max_depth=6, learning_rate=0.1,
                                      min_samples_leaf=3, max_features=1.0)

estimator.fit(X_train, y_train)
print "Train R-squared: %.2f" %estimator.score(X_train, y_train)
print "Test R-squared: %.2f" %estimator.score(X_test, y_test)