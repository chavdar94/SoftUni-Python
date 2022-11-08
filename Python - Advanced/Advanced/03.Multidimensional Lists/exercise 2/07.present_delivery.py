count_of_presents = int(input())
size = int(input())
matrix = []

santa_pos = []
nice_kids = 0
nice_kids_visited = 0

for row in range(size):
    line = input().split()
    if 'S' in line:
        santa_pos = [row, line.index('S')]
    nice_kids += line.count('V')
    matrix.append(line)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while count_of_presents > 0:
    command = input()
    if command == 'Christmas morning':
        break

    row, col = santa_pos[0] + directions[command][0], santa_pos[1] + directions[command][1]
    matrix[santa_pos[0]][santa_pos[1]] = '-'

    if matrix[row][col] == 'V':
        nice_kids_visited += 1
        count_of_presents -= 1

    elif matrix[row][col] == 'C':
        for direction in directions:
            new_row = row + directions[direction][0]
            new_col = col + directions[direction][1]
            if matrix[new_row][new_col] != '-':
                if matrix[new_row][new_col] == 'V':
                    nice_kids_visited += 1
                matrix[new_row][new_col] = '-'
                count_of_presents -= 1

    matrix[row][col] = 'S'

    santa_pos = [row, col]

if count_of_presents == 0 and nice_kids > nice_kids_visited:
    print('Santa ran out of presents!')

for row in matrix:
    print(*row)

if nice_kids_visited == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_visited} nice kid/s.")
