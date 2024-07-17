import yfinance as yf
import pandas as pd
import os

# put the tickers you want to download here
stock_tickers = ["AAPL", "MSFT", "TSLA", "NVDA"]

# how far back to get stock data?
period="5y"

# create data folder
if not os.path.exists("./data"):
  os.mkdir("./data")

# download tickers
data = yf.download(stock_tickers, period=period, actions=True)

for ticker_name in stock_tickers:
  ticker_data = data.xs(ticker_name, level=1, axis=1)

  ticker_data.to_csv("./data/" + ticker_name + ".csv")

  last_quote = ticker_data['Close'].iloc[-1]

  print("Last Price of " + ticker_name + ": $" + str(round(last_quote, 2)))
