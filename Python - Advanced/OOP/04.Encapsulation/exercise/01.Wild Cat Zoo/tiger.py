from project.animal import Animal


class Tiger(Animal):
    MONEY_TO_CARE = 45

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, Tiger.MONEY_TO_CARE)
