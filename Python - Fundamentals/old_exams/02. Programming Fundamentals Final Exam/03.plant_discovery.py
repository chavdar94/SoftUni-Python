def valid_name(plants_dict, name):
    if name not in plants_dict:
        print('error')
        return
    return True


def add_plant(plants_dict):
    plant_info = input().split('<->')
    name = plant_info[0]
    rarity = int(plant_info[1])
    plants_dict[name] = {'rarity': rarity, 'rating': []}
    return plants_dict


def rate(plants_dict, plant, rating):
    if valid_name(plants_dict, plant):
        plants_dict[plant]['rating'].append(rating)
    return plants_dict


def update(plants_dict, plant, new_rarity):
    if valid_name(plants_dict, plant):
        plants_dict[plant]['rarity'] = new_rarity
    return plants_dict


def reset(plants_dict, plant):
    if valid_name(plants_dict, plant):
        plants_dict[plant]['rating'].clear()
    return plants_dict


def print_info(plants_dict):
    print('Plants for the exhibition:')
    for current_plant in plants_dict:
        avg_sum = 0.00
        if sum(plants_dict[current_plant]['rating']) > 0:
            avg_sum = sum(plants_dict[current_plant]['rating']) / len(plants_dict[current_plant]['rating'])
        print(f'- {current_plant}; Rarity: {plants_dict[current_plant]["rarity"]}; Rating: {avg_sum:.2f}')


plants = {}
number = int(input())

for _ in range(number):
    add_plant(plants)

while True:
    command = input()
    if command == 'Exhibition':
        break
    new_command = command.split(': ')
    current_command = new_command[0]
    if current_command == 'Rate':
        plant, rating = new_command[1].split(' - ')
        rate(plants, plant, float(rating))
    elif current_command == 'Update':
        plant, new_rarity = new_command[1].split(' - ')
        update(plants, plant, float(new_rarity))
    elif current_command == 'Reset':
        plant = new_command[1]
        reset(plants, plant)

print_info(plants)
