#!/usr/bin/env python3

import urllib.request, json, locale, re

with urllib.request.urlopen("https://api.bitvalor.com/v1/ticker.json") as url:

    data = json.loads(url.read().decode())
    last = data['ticker_24h']['exchanges']['MBT']['last']
    high = data['ticker_24h']['exchanges']['MBT']['high']
    low  = data['ticker_24h']['exchanges']['MBT']['low']
    vol  = data['ticker_24h']['exchanges']['MBT']['vol']

    #saida = "R$ {last}".format(last=round(last,2))

    locale.setlocale( locale.LC_ALL, '' )
    locale._override_localeconv = {'mon_thousands_sep': '_'}
    locale._override_localeconv = {'mon_decimal_point': ','}
    locale._override_localeconv = {'currency_symbol': 'R$ '}
    last = locale.currency(last)
    last = last.replace(".", ",")

    f = open("btc.html", "w")
    f.write(last)
    f.close()

    f = open("btc.csv", "w")

    csv = last.replace("R$ ", "")
    csv = re.sub(",.*$", "", csv)

    f.write(csv)
    f.close()
    #print(last)
