from collections import deque

elves = deque(int(x) for x in input().split())
presents = [int(x) for x in input().split()]

info = {
    'energy_used': 0,
    'created_toys': 0,
    'counter': 0,
}


def create_toy(energy, box, toys):
    elves.append(energy - (box - 1))
    info['created_toys'] += toys
    info['energy_used'] += box


def third_time(energy, box):
    create_toy(energy, box, 2)


def fifth_time(energy, box):
    elves.append(energy - box)
    info['energy_used'] += box


def not_enough_energy(energy, box):
    elves.append(energy * 2)
    presents.append(box)


def multiply_turns(energy, box, turn_time, adding_box=False):
    multiply_box = box
    if adding_box:
        multiply_box = box * 2
    if energy >= multiply_box:
        if turn_time == 5:
            fifth_time(energy, multiply_box)
        if turn_time == 3:
            third_time(energy, multiply_box)
    else:
        not_enough_energy(energy, box)


while elves and presents:

    elf = elves.popleft()
    if elf < 5:
        continue

    info['counter'] += 1
    box = presents.pop()

    if info['counter'] % 3 == 0 and info['counter'] % 5 == 0:
        multiply_turns(elf, box, 5, True)
    elif info['counter'] % 3 == 0:
        multiply_turns(elf, box, 3, True)
    elif info['counter'] % 5 == 0:
        multiply_turns(elf, box, 5)
    elif box > elf:
        not_enough_energy(elf, box)
    else:
        create_toy(elf, box, 1)

print(f'Toys: {info["created_toys"]}')
print(f'Energy: {info["energy_used"]}')

if elves:
    print(f'Elves left: {", ".join(str(s) for s in elves)}')
if presents:
    print(f'Boxes left: {", ".join(str(s) for s in presents)}')
