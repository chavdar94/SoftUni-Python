first_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest_number(n1, n2, n3):
    numbers = [n1, n2, n3]
    return min(numbers)


print(smallest_number(first_number, second_number, third_number))
