# ==============dict=================
import re

star = r'[s,t,a,r]'
planet_pattern = r'.*@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+).*'
planets = {'Attacked': {'number': 0,
                        'planets': []},
           'Destroyed': {'number': 0,
                         'planets': []},
           }

number_of_messages = int(input())

for msg in range(number_of_messages):
    current_message = input()
    step = len(re.findall(star, current_message, flags=re.I))
    new_message = ''
    for char in current_message:
        new_message += chr(ord(char) - step)
    planet_matches = re.finditer(planet_pattern, new_message)
    for value in planet_matches:
        planet, attack_type = value.group(1), value.group(3)
        if attack_type == 'A':
            planets['Attacked']['number'] += 1
            planets['Attacked']['planets'].append(planet)
        elif attack_type == 'D':
            planets['Destroyed']['number'] += 1
            planets['Destroyed']['planets'].append(planet)

for key in planets:
    print(f'{key} planets: {planets[key]["number"]}')
    if planets[key]["number"] != 0:
        for value in sorted(planets[key]['planets']):
            print(f'-> {value}')

# ==============list=================

# import re
#
# star = r'[s,t,a,r]'
# planet_pattern = r'.*@([A-Z][a-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+).*'
# attacked_planets = []
# destroyed_planets = []
#
# number_of_messages = int(input())
#
# for msg in range(number_of_messages):
#     current_message = input()
#     step = len(re.findall(star, current_message, flags=re.I))
#     new_message = ''
#     for char in current_message:
#         new_message += chr(ord(char) - step)
#
#     planet_matches = re.finditer(planet_pattern, new_message)
#
#     for value in planet_matches:
#         planet, attack_type = value.group(1), value.group(3)
#
#         if attack_type == 'A':
#             attacked_planets.append(planet)
#         elif attack_type == 'D':
#             destroyed_planets.append(planet)
#
# print(f'Attacked planets: {len(attacked_planets)}')
# for planet in sorted(attacked_planets):
#     print(f'-> {planet}')
#
# print(f'Destroyed planets: {len(destroyed_planets)}')
# for planet in sorted(destroyed_planets):
#     print(f'-> {planet}')
