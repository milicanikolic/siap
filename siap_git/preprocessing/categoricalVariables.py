import  pandas as pd

df = pd.read_csv('datasets/withBoroughs.csv')

df = pd.get_dummies(df, columns=['periodOfDay', 'days', 'boroughPickup', 'boroughDropoff'])
df.to_csv('datasets/dummies.csv', index=False)