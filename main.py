import datetime

from pycoingecko import CoinGeckoAPI

from datetime import datetime

# import time

# connect with CoinGeckoAPI
cg = CoinGeckoAPI()

coin = input(f'Enter cryptocurrency: ').lower()

'''
#get current time
t = time.localtime()
current_time = time.strftime("%Y,%m,%d", t)
print(current_time)

#convert datetime to unix timestamp
date_time = datetime.datetime(2022, 9, 29)
unixtime = time.mktime(date_time.timetuple())
print(unixtime)
'''


# get data from CoinGecko (from 2020-01-01 to 2022-09-29)
def get_data():
    data = cg.get_coin_market_chart_range_by_id(id=coin, vs_currency='usd', from_timestamp="1577829600",
                                                to_timestamp='1664398800')
    dict_data = dict(data['prices'])

# change the time format
    x = list(datetime.fromtimestamp(i / 1000).strftime('%Y-%m-%d') for i in dict_data.keys())
    y = list(j for j in dict_data.values())
    res = dict(zip(x, y))

# get min and max value
    min_value = min(res.items(), key=lambda k: k[1])
    max_value = max(res.items(), key=lambda k: k[1])

    return f'{res}; \n min value: {min_value}; \n max value: {max_value}'


print(get_data())
