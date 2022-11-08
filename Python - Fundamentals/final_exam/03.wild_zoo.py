def add(animals_dict, animal_name, needed_food, area):
    if animal_name in animals_dict:
        animals_dict[animal_name]['food'] += needed_food
    else:
        animals_dict[animal_name] = {'food': needed_food, 'area': area}
        areas[area] += 1
    return animals_dict


def add_area(areas, area):
    if area not in areas:
        areas[area] = 0


def feed(animals_dict, animal_name, food):
    if animal_name in animals_dict:
        animals_dict[animal_name]['food'] -= food
        if animals_dict[animal_name]['food'] <= 0:
            print(f'{animal_name} was successfully fed')
            area = animals_dict[animal_name]['area']
            areas[area] -= 1
            del animals_dict[animal_name]


animals_dict = {}
areas = {}

command = input()
while command != 'EndDay':

    command = command.split(': ')
    current_command = command[0]
    if current_command == 'Add':
        animal_name, needed_food, area = [int(x) if x.isdigit() else x for x in command[1].split('-')]
        add_area(areas, area)
        add(animals_dict, animal_name, needed_food, area)

    elif current_command == 'Feed':
        animal_name, food = [int(x) if x.isdigit() else x for x in command[1].split('-')]
        feed(animals_dict, animal_name, food)

    command = input()

print('Animals:')
for animal in animals_dict:
    animal_food = animals_dict[animal]['food']
    print(f' {animal} -> {animal_food}g')

print('Areas with hungry animals:')
for area in areas:
    if areas[area] > 0:
        print(f'{area}: {areas[area]}')
