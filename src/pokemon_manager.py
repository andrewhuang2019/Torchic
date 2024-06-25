import pandas as pd

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


if __name__ == "__main__":
    pokemon_manager = PokemonManager()
    print("teehee")

