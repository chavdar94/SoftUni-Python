rows = int(input())

matrix = [[int(x) for x in input().split()] for x in range(rows)]


primary_diagonal = []
secondary_diagonal = []

for row in range(rows):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][rows - 1 - row])

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)
diff = abs(primary_sum - secondary_sum)
print(diff)
