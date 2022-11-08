def find_bunny():
    for row in range(size):
        if 'B' in matrix[row]:
            return row, matrix[row].index('B')


def check_index(row, col):
    if 0 <= row < size and 0 <= col < size and matrix[row][col] != 'X':
        return True


size = int(input())
matrix = [[int(x) if x[-1].isdigit() else x for x in input().split()] for _ in range(size)]

max_eggs = 0
positions = []
bunny_row, bunny_col = find_bunny()
best_direction = None

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for direction, position in directions.items():
    row = bunny_row + position[0]
    col = bunny_col + position[1]

    path = []
    collected_eggs = 0

    while check_index(row, col):
        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        positions = path
        best_direction = direction

print(best_direction)
print(*positions, sep='\n')
print(max_eggs)
