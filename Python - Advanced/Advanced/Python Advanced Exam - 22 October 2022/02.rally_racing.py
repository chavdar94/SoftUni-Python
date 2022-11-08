size = int(input())
car_name = input()

car_row = 0
car_col = 0
tunnel = {
    'start': [],
    'end': []
}
matrix = []
distance = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for m_row in range(size):
    line = input().split()
    if 'T' in line:
        if not tunnel['start']:
            tunnel['start'] = [m_row, line.index('T')]
        else:
            tunnel['end'] = [m_row, line.index('T')]
    matrix.append(line)

command = input()
while command != 'End':

    row = car_row + directions[command][0]
    col = car_col + directions[command][1]
    car_pos = matrix[row][col]
    if car_pos == '.':
        distance += 10

    elif row == tunnel['start'][0] and col == tunnel['start'][1]:
        matrix[tunnel['start'][0]][tunnel['start'][1]] = '.'
        matrix[tunnel['end'][0]][tunnel['end'][1]] = '.'
        row, col = tunnel['end']
        distance += 30
    elif row == tunnel['end'][0] and col == tunnel['end'][1]:
        matrix[tunnel['end'][0]][tunnel['end'][1]] = '.'
        matrix[tunnel['start'][0]][tunnel['start'][1]] = '.'
        row, col = tunnel['start']
        distance += 30

    if car_pos == 'F':
        distance += 10
        print(f'Racing car {car_name} finished the stage!')
        print(f'Distance covered {distance} km.')
        matrix[row][col] = 'C'
        break

    car_row, car_col = row, col
    command = input()

else:
    print(f'Racing car {car_name} DNF.')
    print(f'Distance covered {distance} km.')
    matrix[car_row][car_col] = 'C'
for p_row in matrix:
    print(*p_row, sep='')