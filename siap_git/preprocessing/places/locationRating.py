import pyproj as proj
from shapely import geometry
import pandas as pd
from statistics import mean

"""
    U ovom fajlu prolayimo kroy veliki data set i za svaku pickup tacku oko nje pravimo krug radiusa 200m,
    i onda prolazimo kroz sve places, koje smo skupili za taj deo grada, i gledamo koja od njih upadaju u 
    napravljeni krug. Te koje upadaju dodajemo u listu i od njih racunamo srednju vrednost rejtinga. Tu srednju
    vrednost upisujemo kao novu kolonu ya svaki red u nasem skupu. 
"""

# setup your projections
crs_wgs = proj.Proj(init='epsg:4326') # assuming you're using WGS84 geographic
crs_bng = proj.Proj(init='epsg:32118') #znaci da cemo raditi sa metrima

df= pd.read_csv('datasets/splitByBoroughs/manhattan.csv')
dfPlaces = pd.read_csv('placesFiles/MANHATTANfiltered.csv')
df['rating'] = ""
cnt = 0

for idx in df.index:
    cnt = cnt + 1
    # then cast your geographic coordinate pair to the projected system
    x, y = proj.transform(crs_wgs, crs_bng, df.loc[idx].pickup_longitude, df.loc[idx].pickup_latitude)
    # create point
    point = geometry.Point(x, y)

    # create your circle buffer from one of the points
    distance = 200
    circle_buffer = point.buffer(distance)
    ratingsForPoint = [] #OVDE CUVAMO REJTINGE OD SVAKE TACKE KOJA UPADA U KRUG TACKE IZ VELIKOG DATA SETA
    for idx2 in dfPlaces.index:
        x2, y2 = proj.transform(crs_wgs, crs_bng, dfPlaces.loc[idx2].longitude, dfPlaces.loc[idx2].latitude)
        # create point
        point2 = geometry.Point(x2, y2)
        # and you can then check if the other point lies within
        if point2.within(circle_buffer):
            ratingsForPoint.append(dfPlaces.loc[idx2].rating)
    if ratingsForPoint:
        srednjaVrednost = mean(ratingsForPoint) #srednja vrednost rejtinga ya okolne tacke, koju cemo upisati u nas skup
        df.set_value(idx, 'rating', srednjaVrednost)
    else:
        df.set_value(idx, 'rating', 0)
    if cnt == 10000:
        print '10000'
        cnt = 0


df.to_csv("datasets/splitByBoroughs/manhattanWithRating.csv", index= False)
