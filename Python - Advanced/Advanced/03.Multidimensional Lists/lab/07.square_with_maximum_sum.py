import sys

rows, cols = tuple(map(int, input().split(', ')))
matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]

max_sum = -sys.maxsize
max_sub_matrix = []
for row in range(rows - 1):
    for col in range(cols - 1):
        sub_matrix = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        current_sum = sum(sub_matrix)

        if sum(sub_matrix) > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix.copy()

print(max_sub_matrix[0], max_sub_matrix[1])
print(max_sub_matrix[2], max_sub_matrix[3])
print(max_sum)