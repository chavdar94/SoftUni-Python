from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Aquarium name cannot be an empty string.')
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish: object):
        if self.capacity == len(self.fish):
            return 'Not enough capacity.'

        if type(fish).__name__ in ('FreshwaterFish', 'SaltwaterFish'):
            self.fish.append(fish)
            return f'Successfully added {type(fish).__name__} to {self.name}.'

    def remove_fish(self, fish: object):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: object):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = [f'{self.name}:']
        if not self.fish:
            result.append('Fish: none')
        else:
            result.append(f'Fish: {" ".join(f.name for f in self.fish)}')

        result.append(f'Decorations: {len(self.decorations)}')
        result.append(f'Comfort: {self.calculate_comfort()}')
        

        return '\n'.join(result)
