dwarves = {}
dwarves_info = []

hat_len = 'hat len'
d_name = 'name'
d_physics = 'physics'
d_hat = 'hat'

dwarf = input()
while dwarf != 'Once upon a time':
    name, color, physics = [int(x) if x.isdigit() else x for x in dwarf.split(' <:> ')]
    if color not in dwarves:
        dwarves[color] = {}
    if name not in dwarves[color]:
        dwarves[color][name] = 0
    if dwarves[color][name] < physics:
        dwarves[color][name] = physics

    dwarf = input()

for color in dwarves:
    for name, points in dwarves[color].items():
        dwarves_info.append({hat_len: len(dwarves[color]), d_name: name, d_physics: points, d_hat: color})
for s_dwarf in sorted(dwarves_info, key=lambda x: (-x[d_physics], -x[hat_len])):
    print(f'({s_dwarf[d_hat]}) {s_dwarf[d_name]} <-> {s_dwarf[d_physics]}')