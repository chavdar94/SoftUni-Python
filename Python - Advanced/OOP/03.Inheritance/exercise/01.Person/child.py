from person import Person


class Child(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

