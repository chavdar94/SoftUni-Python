from abc import ABC, abstractmethod

from project.food import Food, Meat, Vegetable
from project.animals.birds import Owl


class Animal(ABC):
    food_dict = {
        'Hen': {'food': ['Vegetable', 'Fruit', 'Meat', 'Seed'], 'weight_increase': 0.35},
        'Owl': {'food': ['Meat'], 'weight_increase': 0.25},
        'Mouse': {'food': ['Vegetable', 'Fruit'], 'weight_increase': 0.1},
        'Cat': {'food': ['Vegetable', 'Meat'], 'weight_increase': 0.3},
        'Dog': {'food': ['Meat'], 'weight_increase': 0.4},
        'Tiger': {'food': ['Meat'], 'weight_increase': 1}
    }

    def __init__(self, name: str, weight: float, food_eaten: int = 0) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    def feed(self, food: Food):
        animal_type = self.__class__.__name__
        food_type = self.__class__.__name__
        if food_type not in Animal.food_dict[animal_type]['food']:
            return f'{animal_type} does not eat {food_type}'
        self.weight += food.quantity * \
            Animal.food_dict[animal_type]['weight_increase']
        self.food_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size


class Mammal(Animal, ABC):

    def __init__(self, name: str, weight: float, living_region: str) -> None:
        super().__init__(name, weight)
        self.living_region = living_region


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
