#!/usr/bin/python
# Author:Ramazan Yetis
# This script checks the price of BTCUSDT via API in 5 minutes interval and writes the difference of 2 prices into file.

import requests
import time
# Get the exchange rate from API url 
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
# 
def get_exchange_rate():
    response = requests.get(url)
    data = response.json()
    return float(data["price"])

def check_price_change():
    initial_price = get_exchange_rate()
    time.sleep(300)
    final_price = get_exchange_rate()
    return final_price - initial_price

def write_to_file(price_change):
    with open("price_change.txt", "a") as f:
        if price_change > 0:
            f.write("Rates increased by: {}\n".format(price_change))
        elif price_change < 0:
            f.write("Rates decreased by: {}\n".format(abs(price_change)))
        else:
            f.write("Rates remained the same.\n")
while True:
    price_change = check_price_change()
    write_to_file(price_change)
