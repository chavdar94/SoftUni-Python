def absolute_values():
    numbers = input().split()
    float_numbers = [abs(float(num)) for num in numbers]

    return float_numbers


print(absolute_values())
