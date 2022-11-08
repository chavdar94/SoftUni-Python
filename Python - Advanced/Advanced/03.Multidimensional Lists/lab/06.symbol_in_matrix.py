rows = int(input())
matrix = [list(input()) for _ in range(rows)]
searched_symbol = input()

found = False

for row in range(rows):
    for col in range(len(matrix[row])):
        if matrix[row][col] == searched_symbol:
            found = True
            print((row, col))
            break
    if found:
        break

if not found:
    print(f'{searched_symbol} does not occur in the matrix')