import sys

rows, cols = tuple(int(x) for x in input().split())
matrix = [[int(x) for x in input().split()] for x in range(rows)]
sub_matrix = []

max_sum = -sys.maxsize

# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4

for row in range(rows-2):
    for col in range(cols-2):
        first = [matrix[row][col], matrix[row][col+1], matrix[row][col+2]]
        second = [matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]]
        third = [matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]]

        current_total_sum = sum(first) + sum(second) + sum(third)

        if current_total_sum > max_sum:
            max_sum = current_total_sum
            sub_matrix = [first, second, third]
print(f'Sum = {max_sum}')
for row in sub_matrix:
    print(' '.join(str(s) for s in row))