class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self) -> str:
        return f'{self.name} {self.surname}'


class Group:

    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other):
        people = self.people + other.people
        return Group(f'{self.name} {other.name}', people)

    def __repr__(self):
        return f'Group {self.name} with members {", ".join(str(name) for name in self.people)}'

    def __getitem__(self, key):
        return f'Person {key}: {str(self.people[key])}'


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
