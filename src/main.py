import torch
import torch._dynamo
import pandas as pd
import matplotlib.pyplot as plt

torch._dynamo.config.suppress_errors = True

def fn(x):
   a = torch.cos(x)
   b = torch.sin(a)
   return b
new_fn = torch.compile(fn, backend="inductor")
x = torch.randn(10000)
input_tensor = x
a = new_fn(input_tensor)

pokemon_data_frame = pd.read_csv('Pokemon.csv')
moves_data_frame = pd.read_csv('df_moves.csv')
learned_moves_data_frame = pd.read_csv('bridge_pokemon_moves_MAY_LEARN.csv')

print(pokemon_data_frame)
print(moves_data_frame)
print(learned_moves_data_frame)

plt.scatter(x,a)
plt.show()