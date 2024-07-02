from gymnasium import Env 
from gymnasium import spaces 
import numpy as np 
import random
import math

# action values
ATTACK_1 = 0
ATTACK_2 = 1
ATTACK_3 = 2
ATTACK_4 = 3

class PokeEnv(Env):
    def __init__(self):
        self.seed = None
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
        if action in [0,1,2,3]:
            attacks = [1,8,17,25]
        # if action == ATTACK_1:
        #     self.state[1] -= 16
        # elif action == ATTACK_2:
        #     self.state[1] -= 25
        # elif action == ATTACK_3:
        #     self.state[1] -= 10
        # elif action == ATTACK_4:
        #     self.state[1] -= 8
            self.state[1] -= attacks[action]
        else:
            # check for invalid actions
            raise Exception("invalid action")
        #
        # check for win/lose conditions and os.system("cls")lset reward
        #

        print(self.state,end=' ')

        if self.state[1] <= 0:
            reward = 1.0
            self.cumulative_reward += reward
            done = True    
            print(attacks[action])
            # this section is for display purposes
            print(f'Cumulative Reward:  {self.cumulative_reward:.2f}',end='  ')
            print('WIN')
        else:
            dmg = random.randrange(10,25)
            self.state[0] -= dmg
            print(dmg,attacks[action])
            if self.state[0] <= 0:
                reward = -1.0
                self.cumulative_reward += reward 
                done = True
                # this section is for display purposes
                print(f'Cumulative Reward: {self.cumulative_reward:.2f}',end='  ')
                print('LOSE')
        # Update the environment state
        self.cumulative_reward += reward
        return self.state, reward, done, False, info

    def reset(self,seed=None):
        info = {}
        if seed is not None:
            self.seed = seed
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
        return self.state,info
    
    def calc_dmg(self,move,poke1,poke2):
        #             level             critical
        dmg = ((2 * poke1.level * self.crit_hit(poke1.speed))/5) + 2
        #            power            A/D
        dmg = dmg * move.power * (poke1.attack/poke2.defense)
        dmg = (dmg/50) + 2

        # stab
        if move.type == poke1.type1 or (move.type == poke1.type2 and poke1.type2):
            dmg += math.floor(dmg/2)

        # type 1 effectiveness
        dmg *= self.type_effect(move.type,poke2.type1)

        # type 2 effectiveness
        if poke2.type2:
            dmg *= self.type_effect(move.type,poke2.type2)

        # random multiplier
        if dmg == 1:
            return int(dmg)
        else:
            rand = random.randint(217,255)/255
            return int(dmg * rand)
        
    def crit_hit(self,speed):
        thres = min(255,math.floor(speed/2))
        if random.randint(0,255) < thres:
            return 2
        return 1

    def type_effect(self,type1,type2):
        chart = np.loadtxt('chart.csv',dtype=str,delimiter=',')
        i = np.where(chart == type1)[1][0]
        j = np.where(chart == type2)[0][1]
        return chart[i,j]