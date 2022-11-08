def math_operations(*args, **kwargs):
    index = 1
    result = ''

    for num in args:
        if index == 1:
            kwargs['a'] += num
        elif index == 2:
            kwargs['s'] -= num
        elif index == 3:
            if num != 0:
                kwargs['d'] /= num
        elif index == 4:
            kwargs['m'] *= num

        index += 1
        if index > 4:
            index = 1

    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result += f'{key}: {value:.1f}\n'
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# print(math_operations(6.0, a=0, s=0, d=5, m=0))