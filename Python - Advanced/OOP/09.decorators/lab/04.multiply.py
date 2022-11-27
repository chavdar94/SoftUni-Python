def multiply(times):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return result * times
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
