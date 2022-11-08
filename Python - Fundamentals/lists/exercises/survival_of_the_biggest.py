numbers = [int(x) for x in input().split()]
numbers_to_remove = int(input())

for remove in range(numbers_to_remove):
    numbers.remove(min(numbers))

print(", ".join(str(x) for x in numbers))