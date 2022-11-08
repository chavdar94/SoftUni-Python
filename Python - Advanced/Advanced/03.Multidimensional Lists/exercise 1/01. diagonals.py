rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]

# 1, 2, 3
# 4, 5, 6
# 7, 8, 9

primary_diagonal = []
secondary_diagonal = []

for row in range(rows):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][rows - 1 - row])
print(
    f'Primary diagonal: {", ".join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}')
print(
    f'Secondary diagonal: {", ".join([str(s) for s in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}')
