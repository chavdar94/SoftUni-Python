def age_assignment(*args, **kwargs):
    result = {name: 0 for name in args}
    print_result = ''
    for name_letter, age in kwargs.items():
        for name, value in result.items():
            if name.startswith(name_letter):
                result[name] = age
    for name, new_age in sorted(result.items()):
        print_result += f'{name} is {new_age} years old.\n'

    return print_result


# print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))