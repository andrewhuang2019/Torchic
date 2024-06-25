from gymnasium import Env 
from gymnasium import spaces 
import numpy as np 
import random
import os

# action values
ATTACK_1 = 0
ATTACK_2 = 1
ATTACK_3 = 2
ATTACK_4 = 3

class PokeEnv(Env):
    def __init__(self):
        self.cumulative_reward = 0
        self.state = [0,0]   # p1 health, p2 health
        p1_hp = random.randrange(25,150)
        p2_hp = random.randrange(25,150)
        self.state[0] = p1_hp
        self.state[1] = p2_hp 
        self.state = np.array(self.state, dtype=np.int16)
        # observation space (valid ranges for observations in the state)
        self.observation_space = spaces.Box(0, 250, [2,], dtype=np.int16)
        # moves 0-3
        self.action_space = spaces.Discrete(4)
    
    def step(self, action):
        # placeholder for debugging information
        info = {}
        # set default values for done, reward, and the player position
        #before taking the action
        done = False
        reward = -0.01
        #
        # take the action by moving the player
        #
        # this section can be a bit confusing, but 
        # just trust that they move the agent and prevent 
        # it from moving off of the grid
        #
        if action == ATTACK_1:
            self.state[1] -= 16
        elif action == ATTACK_2:
            self.state[1] -= 25
        elif action == ATTACK_3:
            self.state[1] -= 10
        elif action == ATTACK_4:
            self.state[1] -= 8
        else:
            # check for invalid actions
            raise Exception("invalid action")
        #
        # check for win/lose conditions and os.system("cls")lset reward
        #
        if self.state[1] <= 0:
            reward = 1.0
            self.cumulative_reward += reward
            done = True    

            # this section is for display purposes
            os.system("clear")
            print(f'Cumulative Reward: {self.cumulative_reward}')
            print('YOU WIN!!!!')
        else:
            self.state[0] -= random.randrange(0,25)
            if self.state[0] <= 0:
                reward = -1.0
                self.cumulative_reward += reward 
                done = True
                # this section is for display purposes
                os.system("clear")
                print(f'Cumulative Reward: {self.cumulative_reward}')
                print('YOU LOSE')
        # Update the environment state
        self.cumulative_reward += reward
        return self.state, reward, done, info

    def reset(self):
        self.cumulative_reward = 0
        #
        # set the initial state to a flattened 6x6 grid with a randomly 
        # placed entry, win, and player
        #
        self.state = [0,0] 
        p1_hp = random.randrange(25,150)
        p2_hp = random.randrange(25,150)
        self.state[0] = p1_hp
        self.state[1] = p2_hp        
 
        # convert the python array into a numpy array 
        self.state = np.array(self.state, dtype=np.int16)
        return self.state


    def render(self):
        os.system("clear")
        print(f'Cumulative Reward: {self.cumulative_reward}')
        print(f'P1 hp: {self.state[0]}')
        print(f'P2 hp: {self.state[1]}')
     