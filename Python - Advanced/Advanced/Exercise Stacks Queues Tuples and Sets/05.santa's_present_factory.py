from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

presents = {
    'Doll': [150, 0],
    'Wooden train': [250, 0],
    'Teddy bear': [300, 0],
    'Bicycle': [400, 0],
}

while materials and magic_values:
    material = materials.pop()
    magic = magic_values.popleft()

    if magic == 0 and material == 0:
        continue
    elif magic == 0:
        materials.append(material)
        continue
    elif material == 0:
        magic_values.appendleft(magic)
        continue

    current_value = material * magic
    if current_value < 0:
        materials.append(material + magic)
    else:
        is_found = False
        for gift, values in presents.items():
            item_magic, count = values
            if item_magic == current_value:
                presents[gift][1] += 1
                is_found = True
                break
        if current_value > 0 and not is_found:
            materials.append(material + 15)

if (presents['Bicycle'][1] >= 1 and presents['Teddy bear'][1] >= 1) or \
        (presents['Doll'][1] >= 1 and presents['Wooden train'][1] >= 1):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(s) for s in materials[::-1])}")
if magic_values:
    print(f"Magic left: {', '.join(str(s) for s in magic_values)}")

for key, value in sorted(presents.items()):
    _, amount = value
    if amount >= 1:
        print(f"{key}: {amount}")
