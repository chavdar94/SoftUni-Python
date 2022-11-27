from itertools import permutations


def possible_permutations(numbers):
    for num in permutations(numbers):
        yield list(num)


[print(n) for n in possible_permutations([1, 2, 3])]
