import pandas as pd
import matplotlib.pyplot as plt

dfCorr = pd.read_csv('datasets/dummies.csv')

corrMatrix = dfCorr.corr()
corrMatrix.to_csv('correlationMatrixDummies.csv', index = False)
plt.matshow(corrMatrix)
plt.xticks(range(len(dfCorr.columns)), dfCorr.columns)
plt.yticks(range(len(dfCorr.columns)), dfCorr.columns)
plt.colorbar()
plt.show()
