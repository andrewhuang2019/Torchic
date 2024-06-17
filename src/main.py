import torch
import pandas as pd

def main():
    x = torch.rand(5,3)
    print(x)
    frame = pd.DataFrame([1,1])
    print(frame)

main()

