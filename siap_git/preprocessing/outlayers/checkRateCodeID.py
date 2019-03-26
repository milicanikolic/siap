import pandas as pd

df=pd.read_csv('datasets/filteredTrain.csv')

print df.shape

standard = df[(df['RatecodeID'] == 1)]
print 'standard', standard.shape

jfk = df[(df['RatecodeID'] == 2)]
print 'JFK', jfk.shape
newark = df[(df['RatecodeID'] == 3)]
print 'Newark', newark.shape
nw = df[(df['RatecodeID'] == 4)]
print 'Nassau or Westchester', nw.shape
negotiated = df[(df['RatecodeID'] == 5)]
print 'negotiated', negotiated.shape
group = df[(df['RatecodeID'] == 6)]
print 'group', group.shape

df = df[(df['RatecodeID'] == 1) | (df['RatecodeID'] == 2) | (df['RatecodeID'] == 5)]
#df.to_csv('datasets/filteredTest.csv', index = False)
