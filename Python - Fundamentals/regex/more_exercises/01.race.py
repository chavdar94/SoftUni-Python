import re

name_pattern = r'[a-zA-Z]+'
distance_pattern = r'[0-9]'


names = {name.replace(' ', ''): 0 for name in input().split(',')}
command = input()
while command != 'end of race':
    name_match = ''.join(re.findall(name_pattern, command))
    distance_match = sum(int(x) for x in re.findall(distance_pattern, command))

    if name_match in names.keys():
        names[name_match] += distance_match
    command = input()
names = sorted(names.items(), key=lambda x: -x[1])

print(f"1st place: {names[0][0]}")
print(f"2nd place: {names[1][0]}")
print(f"3rd place: {names[2][0]}")