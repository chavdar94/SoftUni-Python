n = int(input())

periodic_table = set()

for _ in range(n):
    element = input().split()
    for el in element:
        periodic_table.add(el)
[print(el) for el in periodic_table]