rows = 6

matrix = [input().split() for _ in range(rows)]
row, col = [int(x) for x in input()[1:-1].split(',')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == 'Stop':
        break

    command = command.split(', ')
    current_command = command[0]
    direction = command[1]

    new_row = row + directions[direction][0]
    new_col = col + directions[direction][1]

    if current_command == 'Create':
        value = command[2]
        if matrix[new_row][new_col] == '.':
            matrix[new_row][new_col] = value

    elif current_command == 'Update':
        value = command[2]
        if matrix[new_row][new_col].isalnum():
            matrix[new_row][new_col] = value

    elif current_command == 'Delete':
        if matrix[new_row][new_col].isalnum():
            matrix[new_row][new_col] = '.'

    elif current_command == 'Read':
        if matrix[new_row][new_col].isalnum():
            print(matrix[new_row][new_col])

    row = new_row
    col = new_col
for row in matrix:
    print(*row)