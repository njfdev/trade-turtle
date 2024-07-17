from stable_baselines3 import PPO
import pandas as pd

from downloader import download_tickers
from gym_env import TradingEnv


# put the tickers you want to download here
stock_tickers = ["AAPL", "MSFT", "TSLA", "NVDA"]
download_tickers(stock_tickers)

aapl_data = pd.read_csv("./data/AAPL.csv", index_col="Date", parse_dates=True)
df = aapl_data[["Open", "High", "Low", "Close", "Volume"]]
# normalize values to range of 0-1
df = (df - df.min()) / (df.max() - df.min())

env = TradingEnv(df)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1_000_000)