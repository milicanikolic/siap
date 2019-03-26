import pandas as pd
import numpy as np

""""
    Podela velikog skupa na 5 razlicitih, po oblastima Njujorka.
"""

df= pd.read_csv('datasets/withBoroughStart.csv')


manhattan = df[(df['boroughPickup'] == "Manhattan")]
print 'Manhattan', manhattan.shape
manhattan.to_csv("datasets/manhattan.csv", index=False)

brooklyn = df[(df['boroughPickup'] == "Brooklyn")]
print 'Brooklyn', brooklyn.shape
brooklyn.to_csv("datasets/brooklyn.csv", index=False)

bronx = df[(df['boroughPickup'] == "Bronx")]
print 'Bronx', bronx.shape
bronx.to_csv("datasets/bronx.csv", index=False)

queens = df[(df['boroughPickup'] == "Queens")]
print 'Queens', queens.shape
queens.to_csv("datasets/queens.csv", index=False)

si = df[(df['boroughPickup'] == "Staten Island")]
print 'Staten Island', si.shape
si.to_csv("datasets/statenIsland.csv", index=False)




