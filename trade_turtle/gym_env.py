import gymnasium as gym
from gymnasium import spaces
import numpy as np

class TradingEnv(gym.Env):
  def __init__(self, df):
    super(TradingEnv, self).__init__()
    self.df = df
    self.current_step = 0

    # define ovservation space (for now, it will be very simple)
    self.action_space = spaces.Discrete(3) # buy, hold, sell
    self.observation_space = spaces.Box(low=0, high=1, shape=(len(df.columns),), dtype=np.float32)

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

    if (action > 0.5):
      reward = -0.5
    elif (action < -0.5):
      reward = 1

    return reward
  
  def render(self, mode="human", close=False):
    pass