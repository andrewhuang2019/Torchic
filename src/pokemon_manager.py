import pandas as pd
import random

class PokemonManager:
    def __init__(self):
        self.pokedex = pd.read_csv("Pokemon.csv", nrows=151)
        print(self.pokedex)

    def get_column(self, input):
        if isinstance(input, bool):
            raise TypeError("Invalid Type")
        elif isinstance(input, int):
            return self.pokedex.iloc[:, input]
        elif isinstance(input, str):
            return self.pokedex[input]
        else:
            raise TypeError("Invalid Type")
    
    def get_random_pokemon(self):
        return self.pokedex.iloc[random.randint(1, 151)]


if __name__ == "__main__":
    pokemon_manager = PokemonManager()
    print(pokemon_manager.get_random_pokemon())

