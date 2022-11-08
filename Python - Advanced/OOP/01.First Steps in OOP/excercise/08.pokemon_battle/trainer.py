from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        for i in range(len(self.pokemons)):
            if self.pokemons[i].username == pokemon.username:
                return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.username} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        for pokemon_info in self.pokemons:
            if pokemon_name == pokemon_info.username:
                self.pokemons.remove(pokemon_info)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = [f'Pokemon Trainer {self.name}', f'Pokemon count {len(self.pokemons)}']
        for _, info in enumerate(self.pokemons):
            result.append(f'- {info.username} with health {info.health}')
        return '\n'.join(result)



pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
