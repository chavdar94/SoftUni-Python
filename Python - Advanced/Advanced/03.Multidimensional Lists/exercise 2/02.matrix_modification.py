def valid_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    print('Invalid coordinates')


def modify_matrix(matrix, numbers, operator):
    row, col, value = numbers
    if valid_index(row, col):
        if operator == 'Add':
            matrix[row][col] += value
        else:
            matrix[row][col] -= value


size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input()
while command != 'END':

    # command = command.split()
    # operator = command[0]
    # numbers = []
    # for num in command[1:]:
    #     numbers.append(int(num))
    operator, *numbers = [int(x) if x[-1].isdigit() else x for x in command.split()]
    modify_matrix(matrix, numbers, operator)
    command = input()

for row in matrix:
    print(*row)
