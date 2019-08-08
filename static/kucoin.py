#!/usr/bin/env python3


import urllib.request, json 
import os

kcsbtc = "0"

os.system("wget -O tick https://api.kucoin.com/api/v1/market/stats?symbol=KCS-BTC 2>/dev/null")
with open('tick', 'r') as myfile:

    url = myfile.read()
    #print(url)
    #data = json.loads(url.read().decode())
    data = json.loads(url)
    kcsbtc = data['data']['last']

    f = open("kcs.csv", "w")
    out = str(kcsbtc)
    out = out.replace(".", "#")
    f.write(out)
    f.close()

