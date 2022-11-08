number_of_dragons = int(input())
dragons = {}
damage_d, health_d, armor_d = "damage", "health", "armor"


def add_dragon(dct, dragon_type, dragon_name, damage, health, armor):
    dct[dragon_type] = dct.get(dragon_type, {})
    dct[dragon_type][dragon_name] = dct[dragon_type].get(dragon_name, {})
    dct[dragon_type][dragon_name][damage_d] = damage
    dct[dragon_type][dragon_name][health_d] = health
    dct[dragon_type][dragon_name][armor_d] = armor


def sort_dragons(dct):
    for color in dct:
        damage, health, armor = 0, 0, 0
        for name in dct[color]:
            damage += dct[color][name][damage_d]
            health += dct[color][name][health_d]
            armor += dct[color][name][armor_d]
        total_dragons = len(dct[color])
        print(f'{color}::({damage / total_dragons:.2f}/{health / total_dragons:.2f}/{armor / total_dragons:.2f})')
        for name in sorted(dct[color].keys()):
            print(f'-{name} -> damage: {dct[color][name][damage_d]}, health: {dct[color][name][health_d]},'
                  f' armor: {dct[color][name][armor_d]}')


for dragon in range(number_of_dragons):
    dragon_type, dragon_name, damage, health, armor = input().split()
    if damage == "null":
        dragon_damage = 45
    else:
        dragon_damage = int(damage)
    if health == "null":
        dragon_health = 250
    else:
        dragon_health = int(health)
    if armor == "null":
        dragon_armor = 10
    else:
        dragon_armor = int(armor)
    add_dragon(dragons, dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)

sort_dragons(dragons)
