import pandas as pd

dfMan = pd.read_csv('placesFiles/MANHATTANfiltered.csv')
avgMan=dfMan['rating'].mean()

dfBrook = pd.read_csv('placesFiles/BROOKLYNfiltered.csv')
avgBrook=dfBrook['rating'].mean()

dfBronx = pd.read_csv('placesFiles/BRONXfiltered.csv')
avgBronx=dfBronx['rating'].mean()

dfQueens = pd.read_csv('placesFiles/QUEENSfiltered.csv')
avgQueens=dfQueens['rating'].mean()

dfSI = pd.read_csv('placesFiles/STATENISLANDfiltered.csv')
avgSI=dfSI['rating'].mean()


dfData = pd.read_csv('datasets/filteredV4.csv')



maskM = ((dfData['dropoffRating'] == 0) & (dfData['boroughDropoff'] == "Manhattan"))
dataM = dfData[maskM]
dfData.loc[maskM, 'dropoffRating'] = (dataM['dropoffRating'] + avgMan)/2


maskBrook = ((dfData['dropoffRating'] == 0) & (dfData['boroughDropoff'] == "Brooklyn"))
dataBrook = dfData[maskBrook]
dfData.loc[maskBrook, 'dropoffRating'] = (dataBrook['dropoffRating'] + avgBrook)/2


maskBr = ((dfData['dropoffRating'] == 0) & (dfData['boroughDropoff'] == "Bronx"))
dataBr = dfData[maskBr]
dfData.loc[maskBr, 'dropoffRating'] = (dataBr['dropoffRating'] + avgBronx)/2


maskQ = ((dfData['dropoffRating'] == 0) & (dfData['boroughDropoff'] == "Queens"))
dataQ = dfData[maskQ]
dfData.loc[maskQ, 'dropoffRating'] = (dataQ['dropoffRating'] + avgQueens)/2


maskSI = ((dfData['dropoffRating'] == 0) & (dfData['boroughDropoff'] == "StatenIsland"))
dataSI = dfData[maskSI]
dfData.loc[maskSI, 'dropoffRating'] = (dataSI['dropoffRating'] + avgSI)/2


dfData['dropoffRating'] = dfData['dropoffRating'].round(1)

dfData.to_csv('datasets/ratingFixed.csv', index=False)