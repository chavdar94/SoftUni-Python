def user_in_values(dict, name):
    for names in dict.values():
        if name in names:
            return True
    return False


def remove_user(dict, name):
    for users in dict.values():
        if name in users:
            users.remove(name)
    return dict


def change_side(dict, user, side):
    if side not in dict:
        dict[side] = []
    if user_in_values(dict, user):
        remove_user(dict, user)
    dict[side].append(user)
    print(f"{name} joins the {side} side!")
    return dict


def user_side(dict, name, side):
    if side not in dict:
        dict[side] = []
    if not user_in_values(dict, name):
        dict[side].append(name)
    return dict


force = {}
command = input()
while command != "Lumpawaroo":

    if "|" in command:
        side, name = command.split(" | ")
        users = user_side(force, name, side)
    elif "->" in command:
        name, side = command.split(" -> ")
        users = change_side(force, name, side)

    command = input()

for key, value in force.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for name in value:
            print(f"! {name}")
