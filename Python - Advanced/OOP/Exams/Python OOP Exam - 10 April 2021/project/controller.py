from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    valid_aquariums = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium,
    }

    valid_decorations = {
        "Ornament": Ornament, 
        "Plant": Plant,
    }

    valid_fish_types = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish,
    }

    def __find_aquarium(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.valid_aquariums:
            return "Invalid aquarium type."

        new_aquarium = self.valid_aquariums[aquarium_type](aquarium_name)
        self.aquariums.append(new_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.valid_decorations:
            return "Invalid decoration type."

        new_decoration = self.valid_decorations[decoration_type]()
        self.decorations_repository.add(new_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.__find_aquarium(aquarium_name)
        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.valid_fish_types:
            return f"There isn't a fish of type {fish_type}."

        new_aquarium = self.__find_aquarium(aquarium_name)
        if not new_aquarium:
            return
        
        if new_aquarium.capacity == len(new_aquarium.fish):
            return 'Not enough capacity.'

        if fish_type[:-4] not in type(new_aquarium).__name__:
            return "Water not suitable."

        new_fish = self.valid_fish_types[fish_type](fish_name, fish_species, price)
        new_aquarium.add_fish(new_fish)
        return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        if not aquarium:
            return
        
        aquarium.feed()

        return f'Fish fed: {len(aquarium.fish)}'

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        if not aquarium:
            return
        
        fish_sum = 0
        decoration_sum = 0
        if aquarium.fish:
            fish_sum = sum(f.price for f in aquarium.fish)
        if aquarium.decorations:
            decoration_sum = sum(d.price for d in aquarium.decorations)
        
        value = fish_sum + decoration_sum
        return f'The value of Aquarium {aquarium_name} is {value:.2f}.'

    def report(self):
        return '\n'.join(str(aquarium) for aquarium in self.aquariums)
