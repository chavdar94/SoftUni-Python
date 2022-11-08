from collections import deque

bees = deque(int(x) for x in input().split())
necar_values = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

while bees and necar_values:
    current_bee = bees.popleft()
    current_nectar = necar_values.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
        continue
    operation = symbols.popleft()
    if current_nectar > 0:
        total_honey += abs(operators[operation](current_bee, current_nectar))

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(s) for s in bees)}")

if necar_values:
    print(f"Nectar left: {', '.join(str(s) for s in necar_values)}")
