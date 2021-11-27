import os 
import requests
import pandas as pd

# This is a general proof of concept to grab stock data and return it via an api endpoint
# You are limited to three ticker symbols at a time this is a limitation of the endpoint itself

stock_api_key = os.environ['STOCK']
url = 'https://api.stockdata.org/v1/data/quote'
my_stocks = []

for x in range(3):
    stock_symbol = input("Please enter up to 3 stock symbol to search for or type 'q' to quit: ").upper()
    if stock_symbol == "Q":
        break
    else:
        my_stocks.append(stock_symbol)

# Had to make a string that joins together multiple ticker symbols in the array.
my_stocks_string = ",".join(my_stocks)

parameters = {
    'symbols' : my_stocks_string,
    'api_token' : stock_api_key
}

# Create a session object that will hold some parameters across multiple requests.
s = requests.Session()
r = s.get(url, params=parameters)

# This converts the response into a python dict
stock_results = r.json()

# I am grabbing a specific array out of the dict and converting that into a dataframe
df = pd.DataFrame(stock_results['data'])
print(df)
