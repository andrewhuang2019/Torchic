import torch
import pandas as pd
import matplotlib.pyplot as plt
def fn(x):
   a = torch.cos(x)
   b = torch.sin(a)
   return b
new_fn = torch.compile(fn, backend="inductor")
x = torch.randn(10000)
input_tensor = x
a = new_fn(input_tensor)

plt.scatter(x,a)
plt.show()