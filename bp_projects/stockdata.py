import requests
import time

ticker = "DDOG"
api_key = "b7fa84afea6e45609dd289c0f21b9f62"

def get_stock_price(ticker_symbol, api):
    url = "https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    print(response)
    return price

def get_stock_quote(ticker_symbol, api):
    url = "https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response

stockdata = get_stock_quote(ticker, api_key)
stock_price = get_stock_price(ticker, api_key)

exchange = stockdata['exchange']
# exchange = stockdata['exchange']
# currency = stockdata['currency']
# open_price = stockdata['open']
# high_price = stockdata['high']
# low_price = stockdata['low']
# close_price = stockdata['close']
# volume = stockdata['volume']
name = stockdata['name']

print(name, stock_price)