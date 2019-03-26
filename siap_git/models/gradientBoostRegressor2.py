from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import ShuffleSplit, train_test_split
from sklearn.model_selection import GridSearchCV
import pandas as pd


df = pd.read_csv('datasets/dummies.csv')
target = df['tip_amount']
features = df.drop(['tip_amount'], axis=1)

X_train, X_test, y_train, y_test = train_test_split(features, target, train_size=0.8)

def GradientBooster(param_grid, n_jobs):
    estimator = GradientBoostingRegressor()
    cv = ShuffleSplit(n_splits = 10, train_size=0.8)
    classifier = GridSearchCV(estimator= estimator, cv = cv, param_grid = param_grid, n_jobs=n_jobs)
    classifier.fit(X_train, y_train)
    print "Best Estimator learned through GridSearch"
    print classifier.best_estimator_
    return cv, classifier.best_estimator_


if __name__ == '__main__':
    param_grid = {'n_estimators': [100, 500], 'learning_rate': [0.1,0.05,0.02],  # 0.05, 0.02, 0.01],
                  'max_depth': [4, 6],  # 4,6],
                  'min_samples_leaf': [3,5,9,17],  # ,5,9,17],
                  'max_features': [1.0,0.3,0.1]}
    n_jobs = 4
    cv,best_est=GradientBooster(param_grid, n_jobs)