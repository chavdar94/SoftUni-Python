size = int(input())
commands = input().split()

coal = 0
collected_coal = 0
matrix = []
start_row, start_col = 0, 0
movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())
    coal += matrix[row].count('c')
    if 's' in matrix[row]:
        start_row, start_col = row, matrix[row].index('s')

for move in commands:
    new_row, new_col = start_row + movements[move][0], start_col + movements[move][1]
    if not 0 <= new_row < size or not 0 <= new_col < size:
        continue

    symbol = matrix[new_row][new_col]

    if symbol == 'e':
        print(f"Game over! {new_row, new_col}")
        break

    if symbol == 'c':
        matrix[new_row][new_col] = '*'
        collected_coal += 1

    if collected_coal == coal:
        print(f"You collected all coal! {new_row, new_col}")
        break

    start_row, start_col = new_row, new_col
else:
    print(f"{coal - collected_coal} pieces of coal left. {start_row, start_col}")