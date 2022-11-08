def check_index(row, col):
    return 0 <= row < size and 0 <= col < size


def move(direction, steps):
    row = position[0] + (directions[direction][0] * steps)
    col = position[1] + (directions[direction][1] * steps)

    if not check_index(row, col):
        return position
    if matrix[row][col] == 'x':
        return position

    return [row, col]


def shoot(direction):
    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]

    while check_index(row, col):
        if matrix[row][col] == 'x':
            matrix[row][col] = '.'
            return [row, col]

        row += directions[direction][0]
        col += directions[direction][1]


matrix = []

size = 5
targets = 0
targets_hit = 0
targets_positions = []
position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'A' in line:
        position = [row, line.index('A')]
    targets += line.count('x')

number_of_commands = int(input())

for _ in range(number_of_commands):

    command = input().split()
    task = command[0]

    if task == 'move':
        shoot_direction = command[1]
        steps = int(command[2])
        position = move(shoot_direction, steps)
    elif task == 'shoot':
        shoot_dir = command[1]
        current_targets = shoot(shoot_dir)

        if current_targets:
            targets_positions.append(current_targets)
            targets_hit += 1

        if targets_hit == targets:
            print(f'Training completed! All {targets} targets hit.')
            break
else:
    print(f'Training not completed! {targets - targets_hit} targets left.')

for target in targets_positions:
    print(target)
