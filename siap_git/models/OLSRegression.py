import statsmodels.formula.api as sm
import pandas as pd


df = pd.read_csv('datasets/dummiesNew.csv')
df = df.drop(['tpep_pickup_datetime', 'tpep_dropoff_datetime'], axis=1)

res = sm.ols(formula="tip_amount~minutes+trip_distance+passenger_count+RatecodeID+trip_amount+rushHour+days+periodOfDay_afternoon+"
                     "periodOfDay_evening+periodOfDay_morning+periodOfDay_night+boroughPickup_Bronx+boroughPickup_Brooklyn+boroughPickup_Queens+"
                     "boroughPickup_Manhattan+boroughPickup_StatenIsland", data=df).fit()
print(res.params)
print res.summary()
