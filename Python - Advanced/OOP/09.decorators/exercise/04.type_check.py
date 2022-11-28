def type_check(expected_type):
    def decorator(function):
        def wrapper(element):
            if not isinstance(element, expected_type):
                return 'Bad Type'

            return function(element)

        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
