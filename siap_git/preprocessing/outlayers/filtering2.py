import pandas as pd

df = pd.read_csv('datasets/filteredV1.csv')

df = df[df['tip_amount'] <= 100]
df = df[df['trip_amount'] <= 150]
df = df[df['trip_distance'] < 45]

df.to_csv('datasets/filteredV2.csv', index = False)