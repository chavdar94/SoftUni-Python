import re

pattern = r'\|(?P<boss_name>[A-Z]{4,})\|\:\#(?P<title>[a-zA-Z]+ [a-zA-Z]+)\#'

number = int(input())

for _ in range(number):
    boss = input()
    matches = re.findall(pattern, boss)
    if matches:
        for match in matches:
            name = match[0]
            title = match[1]
            strength = len(name)
            armor = len(title)
            print(f'{name}, The {title}')
            print(f'>> Strength: {strength}')
            print(f'>> Armor: {armor}')
    else:
        print('Access denied!')