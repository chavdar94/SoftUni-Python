items = input().split()
bakery = {}

for i in range(0, len(items), 2):
    key = items[i]
    value = items[i + 1]
    bakery[key] = int(value)

print(bakery)