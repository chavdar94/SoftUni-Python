def get_info(**kwargs):
    name, town, age = kwargs.items()
    return f'This is {name[1]} from {town[1]} and he is {age[1]} years old'


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
