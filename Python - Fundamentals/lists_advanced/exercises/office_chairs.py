number_of_rooms = int(input())

has_space = True
free_space = 0
for room in range(1, number_of_rooms + 1):

    command = input().split()
    chairs = int(len(command[0]))
    people = int(command[1])
    if chairs > people:
        free_space += chairs - people
    elif chairs < people:
        needed_chairs = people - chairs
        has_space = False
        print(f"{needed_chairs} more chairs needed in room {room}")
if has_space:
    print(f"Game On, {free_space} free chairs left")
