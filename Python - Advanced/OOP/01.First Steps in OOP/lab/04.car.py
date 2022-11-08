class Car:
    def __init__(self, *args):
        self.name = args[0]
        self.model = args[1]
        self.engine = args[2]

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())
