import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model

df = pd.read_csv('datasets/dummies.csv')
y = df['tip_amount']
dfPca = df.drop(['tip_amount'], axis=1)
X = dfPca.values
X = scale(X)

pca = PCA(n_components=29)
pca.fit(X)
var = np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
print var

#plt.plot(var)
#plt.show()

pca = PCA(n_components=8)
pca.fit(X)
X_new=pca.fit_transform(X)

#print X_new


model = linear_model.LinearRegression()
model.fit(X_new, y)

predictions = model.predict(X_new)


print('Coefficients: \n', model.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y, predictions))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y, predictions))



