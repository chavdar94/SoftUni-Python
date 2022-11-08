from collections import deque

matrix_size = 6
matrix = []

rover_pos = []

for add_row in range(matrix_size):
    line = input().split()
    if 'E' in line:
        rover_pos = [add_row, line.index('E')]
    matrix.append(line)

materials = {
    'water': False,
    'metal': False,
    'concrete': False
}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

out_of_range = (
    (-1, 5),
    (6, 0)
)

commands = deque(input().split(', '))

while commands:
    command = commands.popleft()
    positions = [rover_pos[0] + directions[command][0], rover_pos[1] + directions[command][1]]

    if not 0 <= positions[0] < matrix_size or not 0 <= positions[1] < matrix_size:
        for pos in range(len(positions)):
            for oor_pos in out_of_range:
                if positions[pos] == oor_pos[0]:
                    positions[pos] = oor_pos[1]

    if matrix[positions[0]][positions[1]] == 'R':
        print(f'Rover got broken at {(positions[0], positions[1])}')
        break

    if matrix[positions[0]][positions[1]] == 'W':
        materials['water'] = True
        print(f'Water deposit found at {(positions[0], positions[1])}')

    elif matrix[positions[0]][positions[1]] == 'M':
        materials['metal'] = True
        print(f'Metal deposit found at {(positions[0], positions[1])}')

    elif matrix[positions[0]][positions[1]] == 'C':
        materials['concrete'] = True
        print(f'Concrete deposit found at {(positions[0], positions[1])}')

    rover_pos[0], rover_pos[1] = positions[0], positions[1]

if all(materials.values()):
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
