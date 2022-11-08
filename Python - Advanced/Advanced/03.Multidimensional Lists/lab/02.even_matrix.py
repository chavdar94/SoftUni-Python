rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]

even_matrix = []

for row in range(rows):
    current_matrix = []
    for col in range(len(matrix[row])):
        if matrix[row][col] % 2 == 0:
            current_matrix.append(matrix[row][col])
    even_matrix.append(current_matrix)
print(even_matrix)