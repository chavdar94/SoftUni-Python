input_operator = input()
first_number = int(input())
second_number = int(input())


def calculation(operator, num_1, num_2):
    result = None
    if operator == "multiply":
        result = num_1 * num_2
    elif operator == "divide":
        result = int(num_1 / num_2)
    elif operator == "add":
        result = num_1 + num_2
    elif operator == "subtract":
        result = num_1 - num_2
    return result


print(calculation(input_operator, first_number, second_number))
