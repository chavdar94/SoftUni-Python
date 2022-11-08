def start_spring(**kwargs):
    spring_types = {}
    for key, value in kwargs.items():
        spring_types[value] = spring_types.get(value, [])
        spring_types[value].append(key)

    result = []
    for key_type, obj in sorted(spring_types.items(), key=lambda x: (len(x[0]), x[0])):
        result.append(f'{key_type}:')
        for val in sorted(obj):
            result.append(f'-{val}')

    return '\n'.join(result)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


