from __future__ import print_function
from uszipcode import ZipcodeSearchEngine
import pandas as pd
import numpy as np

""""
    U ovom fajlu odredjujemo iy kog od 5 delova njujorka je yapoceta voznja. To radimo kako bismo podelili posao na vise fajlova.
    Pomocu geocodera smo prvo pokusali da izvucemo postanske brojeve za svaku tacku u nasem skupu, ali je pucalo zbog limita od 
    2500 poziva dnevno, a mi imamo 5 500 000. Potom smo nasli bazu sa postanskim kodovima USA, i pomocu nje smo iyvukli postanski kod
    a potom ya svaki postanski kod nasli kom delu Njujorka pripada. Na osnovu toga smo podelili skup na 5 delova: Menheten, Bruklin,
    Bronks, Kvins, Staten Island.
"""

df=pd.read_csv('datasets/filteredV2.csv')
"""
conditions = [
    (10286 >= (geocoder.osm(df.pickup, method='reverse')).json['postal'] >= 10001),
    (10475 >= (geocoder.osm(df.pickup, method='reverse')).json['postal'] >= 10451),
    (11256 >= (geocoder.osm(df.pickup, method='reverse')).json['postal'] >= 11201),
    (10314 >= (geocoder.osm(df.pickup, method='reverse')).json['postal'] >= 10301),
    (11120 >= ((geocoder.osm(df.pickup, method='reverse')).json['postal'] >= 11004) | (11697 >= (geocoder.osm(df.pickup, method='reverse')).json['postal'] >= 11351))
    ]
choices = ['Manhattan', 'Bronx', 'Brooklyn', 'Staten Island', 'Queens']
df['boroughPickup'] = np.select(conditions, choices, default=np.nan)

df.to_csv('datasets/withBoroughStart.csv', index=False)
"""

df['boroughPickup']=''
search = ZipcodeSearchEngine()
cnt = 0

for idx in df.index:
    zipCode = (search.by_coordinate(df.loc[idx].pickup_latitude,df.loc[idx].pickup_longitude, radius=1, returns=1))
    if zipCode:
        zipCodeNumber = int(zipCode[0].Zipcode)
        if (zipCodeNumber >= 10001 and zipCodeNumber <= 10286):
            df.set_value(idx, 'boroughPickup', 'Manhattan')
            #print('MANHATTAN')
        elif (zipCodeNumber >= 10451 and zipCodeNumber <= 10475):
            df.set_value(idx, 'boroughPickup', 'Bronx')
            #print('BRONX')
        elif (zipCodeNumber >= 11201 and zipCodeNumber <= 11256 ):
            df.set_value(idx, 'boroughPickup', 'Brooklyn')
            #print('BROOKLYN')
        elif (zipCodeNumber >= 10301 and zipCodeNumber <= 10314):
            df.set_value(idx, 'boroughPickup', 'StatenIsland')
            #print('STATEN')
        elif ((zipCodeNumber >= 11004 and zipCodeNumber <= 11120) or (zipCodeNumber >= 11351 and zipCodeNumber <= 11697)):
            df.set_value(idx, 'boroughPickup', 'Queens')
            #print('QUEENS')
        else:
            df.set_value(idx, 'boroughPickup', np.NaN)
            #print('NAAAAAAAAAAAAAAAN')

    cnt = cnt + 1
    if cnt == 10000:
        cnt=0
        print('PROSAO')
print (df.boroughPickup)

df.to_csv('datasets/withBoroughStart.csv', index=False)







#res = search.by_coordinate(df['pickup_latitude'],df['pickup_longitude'], radius=1, returns=1)
#len(res) # by default 5 results returned

"""for zipcode in res:
    print (zipcode.Zipcode) """