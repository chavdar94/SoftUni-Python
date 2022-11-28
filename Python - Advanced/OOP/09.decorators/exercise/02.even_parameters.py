def even_parameters(function):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg % 2 != 0:
                return 'Please use only even numbers!'
        else:
            return function(*args)

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
