from googleplaces import GooglePlaces,types,lang
import time
import pandas as pd
import json
from pandas.io.json import json_normalize


"""
Za odredjene tacke uzimamo mesta sa Google mapa koje su u blizini. Kao rezultat dobija se 60 mesta, pa smo delili na vise sitnijih
tacaka u okviru svakog okruga Njujorka (na papiru napisane koje smo tacke uzeli)
"""

gp= GooglePlaces(api_key='AIzaSyB_NaKqSwUSD_DDSkReMz9fycq96ph9VhE')
query_result = gp.nearby_search(location="Murray Hill, Manhattan, New York, NY, USA")
fetched=0
MAX_FETCH= 50000
df = pd.DataFrame(columns= ['place_id', 'name', 'latitude', 'longitude', 'rating'])

def get_nested(data, *args):
    if args and data:
        element = args[0]
        if element:
            value = data.get(element)
            return value if len(args) == 1 else get_nested(value, *args[1:])

while fetched< MAX_FETCH:
    for place in query_result.places:
        place.get_details()
        id = place.place_id
        name = place.name
        rating = place.rating
        lat = get_nested(place.details, "geometry", "location", "lat")
        lng = get_nested(place.details, "geometry", "location", "lng")
        df = df.append({
            'place_id':id, 'name': name, 'latitude':lat, 'longitude':lng, 'rating':rating
        }, ignore_index=True)
        fetched=fetched+1
    if query_result.has_next_page_token:
        time.sleep(3)
        query_result= gp.nearby_search(pagetoken=query_result.next_page_token)

df.to_csv("MANHATTANja11places.csv", index=False, encoding="UTF-8")