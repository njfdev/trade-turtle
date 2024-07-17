import gym
from gym import spaces
import numpy as np

class TradingEnv(gym.Env):
  def __init__(self):
    super(TradingEnv, self).__init__()

    # define ovservation space (for now, it will be very simple)
    self.action_space = spaces.Discrete(3) # buy, hold, sell
    self.observation_space = spaces.Box(low=0, high=1, shape=(10,), dtype=np.float32)

  def reset(self):
    return np.random.rand(10)
  
  def step(self, action):
    state = np.random.rand(10)
    reward = np.random.rand() - 0.5
    done = False
    info = {}
    return state, reward, done, info