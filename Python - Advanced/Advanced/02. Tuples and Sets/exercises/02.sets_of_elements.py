data = list(map(int, input().split()))

first, second = data
first_set = set()
second_set = set()

for i in range(first + second):
    number = input()
    if i < first:
        first_set.add(number)
    else:
        second_set.add(number)

same_elements = first_set.intersection(second_set)
[print(num) for num in same_elements]