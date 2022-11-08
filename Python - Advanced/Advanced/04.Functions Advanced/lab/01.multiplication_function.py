def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(4, 5, 6, 1, 3))
