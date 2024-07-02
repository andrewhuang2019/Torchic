import pandas as pd
import random

class MoveManager:
    def __init__(self, pokemon):
        self.moves_list = pd.read_csv("bridge_pokemon_moves_MAY_LEARN.csv")
        self.moves_list = self.moves_list[self.moves_list['Pokemon'].str.contains(pokemon, na=False)]

        print(self.moves_list)

    #generates a random move from the pokemon's set of possible moves
    def get_random_move(self):
        return self.moves_list.iloc[random.randint(1, self.moves_list.index.max() - self.moves_list.index.min())]

#for testing
if __name__ == "__main__":
    manager = MoveManager('Abra')
    print(manager.get_random_move())