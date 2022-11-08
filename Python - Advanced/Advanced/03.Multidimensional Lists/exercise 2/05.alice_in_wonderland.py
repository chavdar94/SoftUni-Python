def find_alice():
    for row in range(size):
        if 'A' in matrix[row]:
            a_index = matrix[row].index('A')
            matrix[row][a_index] = '*'
            return row, a_index


def check_valid_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

size = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

start_row, start_col = find_alice()
tea_bags = 0

while tea_bags < 10:
    move = input()

    row = start_row + directions[move][0]
    col = start_col + directions[move][1]

    if not check_valid_index(row, col):
        break

    if isinstance(matrix[row][col], int):
        tea_bags += matrix[row][col]

    start_row = row
    start_col = col
    position = matrix[row][col]

    matrix[row][col] = '*'

    if position == 'R':
        break

if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print('Alice didn\'t make it to the tea party.')
for row in matrix:
    print(*row)
