from pokeEnv import PokeEnv
from stable_baselines3.common.env_checker import check_env

env = PokeEnv()
check_env(env)
# env.render()

# action = int(input("Enter action:"))

# state, reward, done, info = env.step(action)

# while not done:
#     env.render()
#     action = int(input("Enter action: "))
#     state, reward, done, info = env.step(action)