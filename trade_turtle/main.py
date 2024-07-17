from stable_baselines3 import PPO

from downloader import download_tickers
from gym_env import TradingEnv


# put the tickers you want to download here
stock_tickers = ["AAPL", "MSFT", "TSLA", "NVDA"]
download_tickers(stock_tickers)

env = TradingEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)