n = int(input())

even_set = set()
odd_set = set()

for i in range(1, n + 1):
    name = input()
    name_sum = 0
    for ch in name:
        name_sum += ord(ch)

    name_sum = int(name_sum / i)

    if name_sum % 2 != 0:
        odd_set.add(name_sum)
    else:
        even_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
elif sum(odd_set) < sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=', ')