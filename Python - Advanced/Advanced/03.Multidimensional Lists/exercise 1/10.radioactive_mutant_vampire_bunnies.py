def player_pos(matrix, player_position):
    for row in range(len(matrix)):
        if 'P' in matrix[row]:
            player_position = row, matrix[row].index('P')
            break
    return player_position


rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    matrix.append(list(input()))

commands = list(input())

moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

player_position = 0, 0
player_position = player_pos(matrix, player_position)

for command in commands:
    new_row, new_col = player_position[0] + moves[command][0], player_position[1] + moves[command][1]
    if matrix[new_row][new_col] == 'B':
        print(f'dead: {new_row} {new_col}')
        break

    if not 0 <= new_row < len(matrix) or not 0 <= new_col < len(matrix):
        print(f'won: {new_row} {new_col}')
        break
