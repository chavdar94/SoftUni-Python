def neighbour_cells(matrix, row, col):
    possible_cells = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1]
    ]

    result = []
    for neighbour_row, neighbour_col in possible_cells:
        if 0 <= neighbour_row < len(matrix) and 0 <= neighbour_col < len(matrix) \
                and matrix[neighbour_row][neighbour_col] > 0:
            result.append([neighbour_row, neighbour_col])
    return result


size = int(input())
matrix = [[int(x) for x in input().split()] for x in range(size)]
coordinates = input().split()

for coordinate in coordinates:
    row, col = [int(x) for x in coordinate.split(',')]
    power = matrix[row][col]

    if power <= 0:
        continue

    matrix[row][col] = 0

    cells = neighbour_cells(matrix, row, col)
    for n_row, n_col in cells:
        matrix[n_row][n_col] -= power

alive_cells = 0
el_sum = 0
for row in matrix:
    for col in row:
        if col > 0:
            alive_cells += 1
            el_sum += col

print(f'Alive cells: {alive_cells}')
print(f'Sum: {el_sum}')
for row in matrix:
    print(*row, sep=' ')
