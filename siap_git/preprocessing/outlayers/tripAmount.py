import pandas as pd

df = pd.read_csv('datasets/filteredTest.csv')

df['amount'] = df.total_amount - df.tip_amount

df = df.drop('total_amount', 1)

df.to_csv('datasets/filteredTest.csv', index = False)