core_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
condition = False

while True:
    data = input().lower().split()
    for i in range(0, len(data), 2):

        key = data[i + 1]
        value = int(data[i])

        if key in core_materials:
            core_materials[key] += value
            if key == 'shards':
                if core_materials[key] >= 250:
                    print('Shadowmourne obtained!')
                    core_materials[key] -= 250
                    condition = True
                    break
            elif key == 'fragments':
                if core_materials[key] >= 250:
                    print('Valanyr obtained!')
                    core_materials[key] -= 250
                    condition = True
                    break
            elif key == 'motes':
                if core_materials[key] >= 250:
                    print('Dragonwrath obtained!')
                    core_materials[key] -= 250
                    condition = True
                    break
        else:
            if key not in junk_materials:
                junk_materials[key] = 0
            junk_materials[key] += value
    if condition:
        break

for key,value in core_materials.items():
    print(f'{key}: {value}')

for key,value in junk_materials.items():
    print(f'{key}: {value}')