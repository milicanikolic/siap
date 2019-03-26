import pandas as pd
import numpy as np

df = pd.read_csv('datasets/dummiesNew.csv')

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

train.to_csv('datasets/trainDummies.csv', index=False)
test.to_csv('datasets/testDummies.csv', index=False)