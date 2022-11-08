fires = input().split("#")
current_water = int(input())

total_fire = 0
cells_extinguished = []

for current_fire in fires:
    cell = current_fire.split(" = ")
    if current_water < int(cell[1]):
        continue
    if current_water >= int(cell[1]):
        if cell[0] == "High":
            if 81 <= int(cell[1]) <= 125:
                current_water -= int(cell[1])
                total_fire += int(cell[1])
                cells_extinguished.append(cell[1])
        elif cell[0] == "Medium":
            if 51 <= int(cell[1]) <= 80:
                current_water -= int(cell[1])
                total_fire += int(cell[1])
                cells_extinguished.append(cell[1])
        elif cell[0] == "Low":
            if 1 <= int(cell[1]) <= 50:
                current_water -= int(cell[1])
                total_fire += int(cell[1])
                cells_extinguished.append(cell[1])

print("Cells:")
for cell in cells_extinguished:
    print(f" - {cell}")
effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
