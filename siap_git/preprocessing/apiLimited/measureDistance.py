import googlemaps
import pandas as pd
import time
"""
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode('Mountain View, CA')
print(location.raw)
"""
"""
g = geocoder.geonames('The Mercer', maxRows=5)
for result in g:
    print result
    print 'deo'
    print(result.address, result.latlng)


"""
"""g = geocoder.google('Mountain View, CA')
print g.latlng

"""

"""from geopy.distance import vincenty
start_point = (40.76353836, -73.96932983)
end_point = (40.74425125, -73.99568939)
"""


import pandas as pd
import requests

"""df = pd.read_csv('datasets/filteredV2.csv')
info = {'pickup': df.apply(lambda x: str(x.pickup_longitude) +',' + str(x.pickup_latitude), axis=1), 'dropOff': df.apply(lambda x: str(x.dropoff_longitude) +',' + str(x.dropoff_latitude), axis=1)}
dfCoord = pd.DataFrame(data=info)
dfCoord.to_csv('datasets/temp.csv', index = False)
"""

"""df = pd.read_csv('datasets/filteredV2.csv')
dfTemp = pd.read_csv('datasets/temp.csv')

dfMerged = pd.DataFrame(pd.concat([df, dfTemp], axis=1))
dfMerged.to_csv('datasets/merged.csv', index = False)
"""
"""
dfMerged = pd.read_csv('datasets/merged.csv')
#payload = {"steps": "true", "geometries": "geojson"}
#dfMerged['estimated_distance'] = dfMerged.apply(lambda x: ((requests.get('http://router.project-osrm.org/route/v1/driving/'+x.pickup + ';' + x.dropOff,params=payload)).json())['routes'][0]['distance'], axis=1)

cnt  = 0
dfMerged['estimated_distance']=''

for idx in dfMerged.index:
    url = 'http://router.project-osrm.org/route/v1/driving/' + dfMerged.loc[idx].pickup + ';' + dfMerged.loc[idx].dropOff
    payload = {"steps": "true", "geometries": "geojson"}
    response = requests.get(url, params=payload)
    data = response.json()
    meters = data['routes'][0]['distance']
    miles = meters * 0.000621371192
    milesRounded = '%.2f' % round(miles, 2)
    dfMerged.set_value(idx, 'estimated_distance', milesRounded)
    if(cnt == 10000):
        print 'uradio 10 hiljada'
        cnt = 0

dfMerged.to_csv('datasets/filteredV3.csv', index = False)
"""

"""
from mapbox import DirectionsMatrix

dfMerged = pd.read_csv('datasets/merged.csv')
myDistance = DirectionsMatrix(access_token="pk.eyJ1IjoiaWxpdHNlIiwiYSI6ImNpenZmcm11YjAwMGQyd2x1Nm9nd2pqcGUifQ.1PZaOWTVajnQZGeBb_x1Bw")
result=myDistance.matrix([[40.7635383606, -73.969329834], [40.7442512512, -73.9956893921]])
print result

"""


""""
dis = vincenty(start_point, end_point).miles
print dis """
"""
import overpass
api = overpass.API()
response = api.Get('node["name"="The Merce"]')
print response
"""

"""
df = pd.read_csv('datasets/filteredV2.csv')
info = {'pickup': df.apply(lambda x: str(x.pickup_latitude) +',' + str(x.pickup_longitude), axis=1), 'dropOff': df.apply(lambda x: str(x.dropoff_latitude) +',' + str(x.dropoff_longitude), axis=1)}
dfCoord = pd.DataFrame(data=info)
dfCoord.to_csv('datasets/temp.csv', index = False)
"""

"""
gmaps = googlemaps.Client(key='AIzaSyB_NaKqSwUSD_DDSkReMz9fycq96ph9VhE')
df = pd.read_csv('datasets/filteredV2.csv')
dfTemp = pd.read_csv('datasets/temp.csv')

dfMerged = pd.DataFrame(pd.concat([df, dfTemp], axis=1))
dfMerged.to_csv('datasets/merged.csv', index = False)

dfMerged['estimated_distance'] = ''
cnt  = 0

for index, row in dfMerged.iterrows():
    row['estimated_distance'] = gmaps.distance_matrix(row['pickup'], row['dropOff'], mode = 'driving')
    cnt = cnt +1
    if(cnt == 9):
        print 'proso'
        time.sleep(1)
        cnt = 0
    if(index == 2400):
        break

dfMerged.to_csv('datasets/filteredV3.csv', index = False) 
""" """"""
"""import requests
source_coordinates = '-73.969329834,40.7635383606;'
dest_coordinates = '-73.9956893921,40.7442512512'
url =  'http://router.project-osrm.org/route/v1/driving/'+source_coordinates+dest_coordinates

payload = {"steps":"true","geometries":"geojson"}

response = ((requests.get('http://router.project-osrm.org/route/v1/driving/'+source_coordinates+dest_coordinates,params=payload)).json())['routes'][0]['distance']
print response
#data = response.json()
#meters = data['routes'][0]['distance']
#miles = meters * 0.000621371192
#miles = '%.2f' % round(miles, 2)
#print(miles)
"""