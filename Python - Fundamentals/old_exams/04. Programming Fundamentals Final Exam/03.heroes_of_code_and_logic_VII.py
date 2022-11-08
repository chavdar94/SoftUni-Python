def add_heroes(dict, hero_info):
    name, hp, mp = [int(x) if x.isdigit() else x for x in hero_info.split()]
    if hp <= 100 and mp <= 200:
        dict[name] = {'hp': hp, 'mp': mp}


def hero_validation(dict, name):
    if name in dict:
        return True
    return False


def cast_spell(dict, hero_name, mp_needed, spell_name):
    if dict[hero_name]['mp'] >= mp_needed:
        dict[hero_name]['mp'] -= mp_needed
        left_mp = dict[hero_name]['mp']
        print(f"{hero_name} has successfully cast {spell_name} and now has {left_mp} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(dict, hero_name, dmg, attacker):
    if dict[hero_name]['hp'] - dmg > 0:
        dict[hero_name]['hp'] -= dmg
        current_hp = dict[hero_name]['hp']
        print(f"{hero_name} was hit for {dmg} HP by {attacker} and now has {current_hp} HP left!")
    else:
        del dict[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")


def recharge(dict, hero_name, mana):
    if dict[hero_name]['mp'] + mana > 200:
        mana = 200 - dict[hero_name]['mp']
        dict[hero_name]['mp'] = 200
    else:
        dict[hero_name]['mp'] += mana
    print(f"{hero_name} recharged for {mana} MP!")


def heal(dict, hero_name, healed):
    if dict[hero_name]['hp'] + healed > 100:
        healed = 100 - dict[hero_name]['hp']
        dict[hero_name]['hp'] = 100
    else:
        dict[hero_name]['hp'] += healed
    print(f"{hero_name} healed for {healed} HP!")


heroes_dict = {}
number_of_heroes = int(input())
for _ in range(number_of_heroes):
    hero = input()
    add_heroes(heroes_dict, hero)

command = input()
while command != 'End':
    command = command.split(' - ')
    current_command = command[0]
    hero_name = command[1]
    if hero_validation(heroes_dict, hero_name):
        if current_command == 'CastSpell':
            mana = int(command[2])
            spell = command[3]
            cast_spell(heroes_dict, hero_name, mana, spell)

        elif current_command == 'TakeDamage':
            damage = int(command[2])
            attacker = command[3]
            take_damage(heroes_dict, hero_name, damage, attacker)

        elif current_command == 'Recharge':
            mana = int(command[2])
            recharge(heroes_dict, hero_name, mana)
        elif current_command == 'Heal':
            healed = int(command[2])
            heal(heroes_dict, hero_name, healed)

    command = input()

for hero in heroes_dict:
    print(hero)
    print(f'  HP: {heroes_dict[hero]["hp"]}')
    print(f'  MP: {heroes_dict[hero]["mp"]}')
