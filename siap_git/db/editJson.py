import json
from decimal import Decimal

jsonoutput = 'db/nyALLFormatted.json'


res = []
cnt = 0

cnt2 = 0

with open('db/nyALL.json') as f:
    for line in f:
        data = json.loads(line)
        cnt = cnt + 1
        cnt2  = cnt2 + 1
        var = [float(data['dropoff_longitude']), float(data['dropoff_latitude'])]
        data['lnglat'] = var
        res.append(data)
        if cnt == 50000:
            print '50000'
            cnt = 0
            with open(jsonoutput, 'a') as f1:
                for x in res:
                    json.dump(x, f1)
                    f1.write('\n')
            res = []

    with open(jsonoutput, 'a') as f1:
        for x in res:
            json.dump(x, f1)
            f1.write('\n')


