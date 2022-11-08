def check_valid_index(row1, col1, row2, col2):
    if 0 <= row1 < rows and 0 <= col1 < cols \
            and 0 <= row2 < rows and 0 <= col2 < cols:
        return True
    print("Invalid input!")


def swap(row1, col1, row2, col2):
    if check_valid_index(row1, col1, row2, col2):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in range(len(matrix)):
            print(" ".join(map(str, matrix[row])))


rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

command = input()
while command != 'END':
    command, *coords = [int(x) if x.isdigit() else x for x in command.split()]
    if command == 'swap' and len(coords) == 4:
        row1, col1, row2, col2 = coords
        swap(row1, col1, row2, col2)
    else:
        print('Invalid input!')

    command = input()
