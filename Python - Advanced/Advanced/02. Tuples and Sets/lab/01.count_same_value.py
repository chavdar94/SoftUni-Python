numbers = tuple(map(float, input().split()))

numbers_dict = {}
for num in numbers:
    if num not in numbers_dict.keys():
        numbers_dict[num] = 0
    numbers_dict[num] += 1

for key, value in numbers_dict.items():
    print(f'{key} - {value} times')