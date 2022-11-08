first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(n1, n2):
    result = n1 + n2
    return result


def subtract(n3):
    sums = sum_numbers(first_number, second_number)
    subtracting = sums - n3
    return subtracting


def add_and_subtract(n1, n2, n3):
    final_result = subtract(third_number)
    return final_result


print(add_and_subtract(first_number, second_number, third_number))
