rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]

result = []

for row in matrix:
    result.extend(row)

print(result)