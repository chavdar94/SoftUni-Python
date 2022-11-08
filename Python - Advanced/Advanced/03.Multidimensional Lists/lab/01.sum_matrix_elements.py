rows, cols = tuple(map(int, input().split(', ')))
matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]

total_sum = 0
for row in range(rows):
    current_sum = 0
    for col in range(cols):
        current_sum += matrix[row][col]
    total_sum += current_sum
print(total_sum)
print(matrix)