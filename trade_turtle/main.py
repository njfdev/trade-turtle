import yfinance as yf

aapl = yf.Ticker("AAPL")

history = aapl.history()
last_quote = history['Close'].iloc[-1]

print("Last Price of AAPL: $" + str(round(last_quote, 2)))