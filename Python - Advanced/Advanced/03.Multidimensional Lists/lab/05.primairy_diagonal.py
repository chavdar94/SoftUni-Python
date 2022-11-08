rows = int(input())
matrix = [[int(x) for x in input().split()] for x in range(rows)]

diagonal_sum = 0
for row in range(rows):
    diagonal_sum += matrix[row][row]
print(diagonal_sum)