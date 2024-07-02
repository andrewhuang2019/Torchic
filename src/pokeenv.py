from gymnasium import Env 
from gymnasium import spaces 
import numpy as np 
import random
import math

from pokemon import Pokemon
from move import Move

# temp initialization of moves and pokemon
move1 = Move('Absorb','Grass',20,'Special')
move2 = Move('Aqua Tail','Water',30,'Physical')
move3 = Move('Barrage','Normal',15,'Physical')
move4 = Move('Bolt Beak','Electric',25,'Physical')

poke1 = Pokemon('Charmander',39,52,60,43,50,65,25,[move1,move2,move3,move4],'Fire')
poke2 = Pokemon('Squirtle',44,48,50,65,64,43,25,[move1,move2,move3,move4],'Water')

class PokeEnv(Env):
    def __init__(self):
        self.seed = None
        self.cumulative_reward = 0
        self.state = [poke1.health,poke2.health]   # p1 health, p2 health
        self.state = np.array(self.state, dtype=np.int16)
        # observation space (valid ranges for observations in the state)
        self.observation_space = spaces.Box(0, 250, [2,], dtype=np.int16)
        # moves 0-3
        self.action_space = spaces.Discrete(4)
    
    def step(self, action):
        info = {}

        done = False
        reward = -0.01

        if action in [0,1,2,3]:
            self.state[1] -= self.calc_dmg(poke1,poke2,poke1.moveset[action])
        else:
            raise Exception("invalid action")

        print(self.state,end=' ')

        if self.state[1] <= 0:
            reward = 1.0
            self.cumulative_reward += reward
            done = True    
            print(poke1.moveset[action].name)
            # this section is for display purposes
            print(f'Cumulative Reward:  {self.cumulative_reward:.2f}',end='  ')
            print('WIN')
        else:
            dmg = random.randrange(0,3)
            self.state[0] -= self.calc_dmg(poke2,poke1,poke2.moveset[dmg])
            print(poke2.moveset[dmg].name, '|', poke1.moveset[action].name)
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
        self.state = [poke1.health,poke2.health] 
 
        # convert the python array into a numpy array 
        self.state = np.array(self.state, dtype=np.int16)
        return self.state,info
    
    def calc_dmg(self,poke1,poke2,move):
        #             level             critical
        dmg = ((2 * poke1.level * self.crit_hit(poke1.speed))/5) + 2
        #            power            
        dmg = dmg * move.power

        # A/D
        if move.dmg_class == 'Special':
            dmg = dmg * (poke1.sp_attack/poke2.sp_defense)
        else:
            dmg = dmg * (poke1.attack/poke2.defense)
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
        
    # crit multiplier based on speed
    def crit_hit(self,speed):
        thres = min(255,math.floor(speed/2))
        if random.randint(0,255) < thres:
            return 2
        return 1

    # type effectiveness multiplier
    def type_effect(self,type1,type2):
        chart = np.loadtxt('chart.csv',dtype=str,delimiter=',')
        i = np.where(chart == type1)[1][0]
        j = np.where(chart == type2)[0][1]
        return float(chart[i,j])