# my solution

# numbers = list(map(int, input().split()))
# target = int(input())
#
# while numbers:
#     first = numbers.pop(0)
#     i = 0
#     if first >= target:
#         continue
#
#     while i < len(numbers):
#         second = numbers[i]
#         if first + second == target:
#             print(f'{first} + {second} = {target}')
#             if i + 1 >= len(numbers):
#                 break
#             else:
#                 first = numbers[i + 1]
#                 numbers.pop(i)
#
#         i += 1


#  softuni first solution:

# numbers = list(map(int, input().split()))
# target = int(input())
#
# for i in range(len(numbers)):
#     if numbers[i] == '':
#         continue
#     for j in range(i+1, len(numbers)):
#         if numbers[j] == '':
#             continue
#         if numbers[i] + numbers[j] == target:
#             print(f'{numbers[i]} + {numbers[j]} = {target}')
#             numbers[i] = ''
#             numbers[j] = ''
#             break

#  softuni second solution:

numbers = list(map(int, input().split()))
target = int(input())

targets = set()
values_map = {}

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f'{pair} + {value} = {target}')
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values_map[resulting_number] = value
