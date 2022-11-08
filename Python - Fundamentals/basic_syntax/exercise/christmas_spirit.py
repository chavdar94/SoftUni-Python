#  12 - Christmas Spirit

quantity = int(input())
days = int(input())

total_cost = 0
spirit = 0
ornaments = 2
tree_skirt = 5
tree_gerland = 3
tree_lights = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += quantity * ornaments
        spirit += 5
    if day % 3 == 0:
        total_cost += (tree_gerland + tree_skirt) * quantity
        spirit += 13
    if day % 5 == 0:
        total_cost += tree_lights * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_cost += tree_lights + tree_skirt + tree_gerland

if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
