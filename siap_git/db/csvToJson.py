
import json
import csv
import pandas as pd
import ijson
import io
"""
df = pd.read_csv('datasets/splitByBoroughs/manhattan.csv')
with open('datasets/manhattan.json', 'w') as f:
    f.write(df.to_json(orient='records', lines=True).replace("}" , "},"))
"""
"""with open('datasets/manhattan.json', 'r') as jsonFile:
    data = json.load(jsonFile)
"""
"""

def load_json(filename):
    with open(filename, 'r') as fd:
        parser = ijson.parse(fd)
        ret = {'builders': {}}
        for prefix, event, value in parser:
            if (prefix, event) == ('builders', 'map_key'):
                buildername = value
                ret['builders'][buildername] = {}
            elif prefix.endswith('.shortname'):
                ret['builders'][buildername]['shortname'] = value

        return ret

data = load_json('datasets/manhattan.json')
"""




f = open('db/allPlacesNY.csv', 'rb')
reader = csv.DictReader(f)


jsonoutput = 'db/nyAllPlaces.json'
with open(jsonoutput, 'a') as f:
    for x in reader:
        json.dump(x, f)
        f.write('\n')
print 'UCITAO JSON'

"""
cnt =0
for place in data:
    cnt =cnt+1
    var = [place['pickup_longitude'], place['pickup_latitude']]
    place['lnglat'] = var
    if(cnt%)


with open('datasets/manhattanLngLat.json', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=4, separators=(",",":"))
"""