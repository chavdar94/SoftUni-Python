def add_city(cities_dict, city, population, gold):
    if city not in cities_dict:
        cities_dict[city] = {'population': population, 'gold': gold}
    else:
        cities_dict[city]['population'] += population
        cities_dict[city]['gold'] += gold
    return cities_dict


def plunder(cities_dict, town, people, gold):
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    cities_dict[town]['population'] -= people
    cities_dict[town]['gold'] -= gold
    if cities_dict[town]['population'] <= 0 or cities_dict[town]['gold'] <= 0:
        print(f"{town} has been wiped off the map!")
        del cities_dict[town]
    return cities_dict


def prosper(cities_dict, town, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
        return
    else:
        cities_dict[town]['gold'] += gold
        total_gold = cities_dict[town]['gold']
        print(f"{gold} gold added to the city treasury. {town} now has {total_gold} gold.")
    return cities_dict


cities = {}
while True:
    command = input()
    if command == 'Sail':
        break
    city, population, gold = [int(x) if x.isdigit() else x for x in command.split('||')]
    add_city(cities, city, population, gold)

while True:
    event = input()
    if event == 'End':
        break
    event = event.split('=>')
    current_event = event[0]
    if current_event == 'Plunder':
        town = event[1]
        people = int(event[2])
        gold = int(event[3])
        plunder(cities, town, people, gold)

    elif current_event == 'Prosper':
        town = event[1]
        gold = int(event[2])
        prosper(cities, town, gold)

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town in cities:
        population = cities[town]['population']
        gold = cities[town]['gold']
        print(f'{town} -> Population: {population} citizens, Gold: {gold} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
