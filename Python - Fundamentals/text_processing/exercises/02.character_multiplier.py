data = input().split()

first = data[0]
second = data[1]
total_sum = 0
difference = abs(len(first) - len(second))

if len(first) > len(second):
    for char in range(len(second)):
        total_sum += ord(first[char]) * ord(second[char])
    for char in range(len(first) - difference, len(first)):
        total_sum += ord(first[char])
elif len(second) > len(first):
    for char in range(len(first)):
        total_sum += ord(second[char]) * ord(first[char])
    for char in range(len(second) - difference, len(second)):
        total_sum += ord(second[char])
else:
    for char in range(len(first)):
        total_sum += ord(first[char]) * ord(second[char])

print(total_sum)

