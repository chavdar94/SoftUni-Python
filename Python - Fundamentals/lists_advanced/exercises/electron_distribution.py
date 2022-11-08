number = int(input())

electron_cells = []

for num in range(1, number + 1):
    electrons = 2 * pow(num, 2)
    if electrons < number:
        electron_cells.append(electrons)
        number -= electrons
electron_cells.append(number)
print(electron_cells)

