import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
fields = ['trip_distance','minutes', 'tip_amount','total_amount','passenger_count','days']
data = pd.read_csv('ds/filteredTrain1.csv', skipinitialspace=True, usecols=fields)

plt.style.use('ggplot')

pd.scatter_matrix(data, alpha=0.2, figsize=(10, 10))

plt.show()

a=[1,2,3,4,5]
b=[4,4,4,4,4]
c=[8,8,8,8,8]

