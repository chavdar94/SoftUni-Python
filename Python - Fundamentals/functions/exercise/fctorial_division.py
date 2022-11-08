from math import factorial


def factorial_func(n1, n2):
    #  Using math library and factorial function with storing the sums in variables
    # if n1 >= 0 and n2 >= 0:
    #     first_fact = factorial(n1)
    #     second_fact = factorial(n2)
    #     return f"{first_fact / second_fact:.2f}"
    #
    #  Using no libraries and also storing the sums in variables ,so we can access each sum separately
    # if n1 >= 0:
    #     first_sum = 1
    #     for i in range(1, n1 + 1):
    #         first_sum *= i
    #
    # if n2 >= 0:
    #     second_sum = 1
    #     for i in range(1, n2 + 1):
    #         second_sum *= i
    # result = first_sum / second_sum
    # return f"{result:.2f}"
    #
    #  Shortest way to find the final result also using math library
    return f"{(factorial(n1) / factorial(n2)):.2f}"


first_number, second_number = int(input()), int(input())
print(factorial_func(first_number, second_number))
