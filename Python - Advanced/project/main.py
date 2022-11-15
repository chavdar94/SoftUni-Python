from project.test import Human


class Male(Human):

    def __init__(self, name) -> None:
        super().__init__(name)


m = Male('TestName')
print(m.is_alive())
print(m.is_walking())
