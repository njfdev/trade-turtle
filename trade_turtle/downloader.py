import yfinance as yf
import pandas as pd
import os

def download_tickers(tickers, period="5y", redownload=False):
  tickers_to_download=[]

  if redownload:
    tickers_to_download=tickers
  else:
    for ticker in tickers:
      if not os.path.exists("./data/" + ticker + ".csv"):
        tickers_to_download.append(ticker)

  if len(tickers_to_download) == 0:
    return

  # create data folder
  if not os.path.exists("./data"):
    os.mkdir("./data")

  # download tickers
  data = yf.download(tickers_to_download, period=period, actions=True)

  for ticker_name in tickers_to_download:
    ticker_data = data.xs(ticker_name, level=1, axis=1)

    ticker_data.to_csv("./data/" + ticker_name + ".csv")

    last_quote = ticker_data['Close'].iloc[-1]

    print("Last Price of " + ticker_name + ": $" + str(round(last_quote, 2)))
