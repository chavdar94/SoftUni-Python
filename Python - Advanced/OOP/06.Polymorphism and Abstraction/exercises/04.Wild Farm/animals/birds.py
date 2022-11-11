from project.animals.animal import Bird


class Owl(Bird):

    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight, wing_size)
    
    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):

    def __init__(self, name: str, weight: float, wing_size: float) -> None:
        super().__init__(name, weight, wing_size)
    
    def make_sound(self):
        return 'Cluck'