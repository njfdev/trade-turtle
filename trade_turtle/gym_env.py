import gymnasium as gym
from gymnasium import spaces
import numpy as np

class TradingEnv(gym.Env):
  def __init__(self, df):
    super(TradingEnv, self).__init__()
    self.df = df
    self.current_step = 0

    # define observation space (for now, it will be very simple)
    self.action_space = spaces.Discrete(3) # buy, hold, sell
    self.observation_space = spaces.Box(low=0, high=1, shape=(len(df.columns),), dtype=np.float32)

    self.positions = {
      "count": 0,
      "avg_price": 0,
    }


  def reset(self, seed=None, options={}):
    super().reset(seed=seed)
    self.current_step = 0
    return self._next_observation(), {}
  
  def _next_observation(self):
    obs = self.df.iloc[self.current_step].values
    return obs
  
  def step(self, action):
    self.current_step += 1

    obs = self._next_observation()

    reward = self._take_action(action, obs)

    done = self.current_step >= len(self.df) - 1

    return obs, reward, done, {}, {}
  
  def _take_action(self, action, obs):
    # for now, just hardcode some values for buy and sell
    reward = 0

    # Actually get this from the df
    stock_price = 5

    # buy action
    if (action > 0.5):
      self.positions = {
        "count": self.positions["count"] + 1,
        "avg_price": ((self.positions["avg_price"] * self.positions["count"]) + stock_price)/(self.positions["count"] + 1)
      }
    elif (action < -0.5):
      self.positions["count"] -= 1
      reward = self.positions["avg_price"] - stock_price

    return reward
  
  def render(self, mode="human", close=False):
    pass

# return 0 if division by 0 rather than error
def divide(n, d):
  return n / d if d else 0