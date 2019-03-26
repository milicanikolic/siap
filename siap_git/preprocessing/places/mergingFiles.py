import pandas as pd

"""
df1 = pd.read_csv('placesFiles/dodatnoManhattan/hellskitchenManhattan.csv')
df1 = df1.drop_duplicates(['place_id'])

df2 = pd.read_csv('placesFiles/dodatnoManhattan/midtownManhattan.csv')
df2 = df2.drop_duplicates(['place_id'])

df3 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja1places.csv')
df3 = df3.drop_duplicates(['place_id'])

df4 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja2places.csv')
df4 = df4.drop_duplicates(['place_id'])

df5 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja3places.csv')
df5 = df5.drop_duplicates(['place_id'])


df6 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja4places.csv')
df6 = df6.drop_duplicates(['place_id'])

df7 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja5places.csv')
df7 = df7.drop_duplicates(['place_id'])

df8 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja6places.csv')
df8 = df8.drop_duplicates(['place_id'])

df9 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja7places.csv')
df9 = df9.drop_duplicates(['place_id'])

df10 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja8places.csv')
df10 = df10.drop_duplicates(['place_id'])

df11 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja9places.csv')
df11 = df11.drop_duplicates(['place_id'])

df12 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja10places.csv')
df12 = df12.drop_duplicates(['place_id'])

df13 = pd.read_csv('placesFiles/dodatnoManhattan/MANHATTANja11places.csv')
df13 = df13.drop_duplicates(['place_id'])

dfAll = pd.read_csv('placesFiles/MANHATTANfiltered.csv')

df = pd.DataFrame(pd.concat([dfAll, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13]))

df =df.drop_duplicates(['place_id'])

df.to_csv('placesFiles/MANHATTAN.csv', index=False)

"""

df1 = pd.read_csv('datasets/boroughsRatings/bronxRatingFixed.csv')
df2 = pd.read_csv('datasets/boroughsRatings/brooklynRatingFixed.csv')
df3 = pd.read_csv('datasets/boroughsRatings/manhattanRatingFixed.csv')
df4 = pd.read_csv('datasets/boroughsRatings/queensRatingFixed.csv')
df5 = pd.read_csv('datasets/boroughsRatings/statenIslandRatingFixed.csv')

df = pd.DataFrame(pd.concat([df1, df2, df3, df4, df5]))

df.to_csv('datasets/filteredV3.csv', index=False)