import pymongo
import pyproj as proj
from shapely import geometry
import pandas as pd
from statistics import mean
from bson.objectid import ObjectId

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['siap']
manhattan = database['manhattan']
manhattanPlaces = database['manhattanPlaces']


cnt = 0

for ppoint in manhattan.find():
    myCursor = list(manhattanPlaces.find({
        'lnglat': {"$geoWithin" : {"$centerSphere" : [ppoint['lnglat'], 0.124274238/3963.2 ]}}
    }, {'rating':1}))

    nearPlaces=[]
    if myCursor:
        for i in myCursor:
            nearPlaces.append(i['rating'])
        avgVal= mean(nearPlaces)
        manhattan.update_one({
            '_id': ppoint['_id']
        },{
            '$set': {
                'rating':avgVal
            }
        })

    cnt = cnt+1
    if cnt == 10000:
        print ('10 HILJADA')
        cnt = 0



