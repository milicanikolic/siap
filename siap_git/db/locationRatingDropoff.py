import pymongo
from statistics import mean
import numpy as np


uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['siap']
ny = database['nyAll']
nyPlaces = database['nyAllPlaces']


cnt = 0
myCursor = np.nan
for ppoint in ny.find():
    myCursor = nyPlaces.find({
        'lnglat': {"$geoWithin" : {"$centerSphere" : [ppoint['lnglat'], 0.124274238/3963.2 ]}}
    }, {'rating':1}, no_cursor_timeout=True)
    myCursorList= list(myCursor)
    nearPlaces=[]
    if myCursorList:
        for i in myCursorList:
            nearPlaces.append(i['rating'])

        avgVal= mean(nearPlaces)
        ny.update_one({
            '_id': ppoint['_id']
        },{
            '$set': {
                'dropoffRating':avgVal
            }
        })

    cnt = cnt+1
    if cnt == 50000:
        print ('50 HILJADA')
        cnt = 0
myCursor.close()


"""
df1 = pd.read_csv('placesFiles/MANHATTANfiltered.csv')
df2 = pd.read_csv('placesFiles/BRONXfiltered.csv')
df3 = pd.read_csv('placesFiles/BROOKLYNfiltered.csv')
df4 = pd.read_csv('placesFiles/QUEENSfiltered.csv')
df5 = pd.read_csv('placesFiles/STATENISLANDfiltered.csv')

df = pd.DataFrame(pd.concat([ df1, df2, df3, df4, df5]))

df.to_csv('db/allPlacesNY.csv', index=False)
"""