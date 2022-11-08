def check_index():
    pass


rows, cols = [int(x) for x in input().split(', ')]

matrix = []
items = {
    'Decorations': [0, 0],
    'Gifts': [0, 0],
    'Cookies': [0, 0],
}

data = {
    'D': 'Decorations',
    'G': 'Gifts',
    'C': 'Cookies'
}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

s_row, s_col = 0, 0

for row in range(rows):
    line = input().split()
    if 'Y' in line:
        s_row, s_col = row, line.index('Y')
    items['Decorations'][0] += line.count('D')
    items['Gifts'][0] += line.count('G')
    items['Cookies'][0] += line.count('C')
    matrix.append(line)

while True:
    command = input()
    if command == 'End':
        break
    direction, steps = [int(x) if x.isdigit() else x for x in input().split('-')]
