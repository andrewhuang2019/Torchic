from gym import Env 
from gym import spaces 
import numpy as np 
import os

# action values
ATTACK_1 = 0
ATTACK_2 = 1
ATTACK_3 = 2
ATTACK_4 = 3

class Pokenv:
    def __init__(self):
        self.cumulative_reward = 0
                    # p1 health, p2 health
        self.state = [0,0]


        self.state = np.array(self.state, dtype=np.int16)
        # observation space (valid ranges for observations in the state)
        self.observation_space = spaces.Box(0, 3, [36,], dtype=np.int16)
        # valid actions:
        #   0 = up
        #   1 = down
        #   2 = left
        #   3 = right
        # spaces.Discrete(4) is a shortcut for defining the actions 0-3
        self.action_space = spaces.Discrete(4)
    
    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self):
        pass