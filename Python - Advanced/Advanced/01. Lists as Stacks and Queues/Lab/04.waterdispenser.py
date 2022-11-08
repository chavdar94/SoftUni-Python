from collections import deque

liters = int(input())
people = deque()

name = input()
while name != 'Start':
    people.append(name)
    name = input()
    
command = input()
while command != 'End':
    if command.isdigit():
        person_liters = int(command)
        if person_liters <= liters:
            print(f'{people.popleft()} got water')
            liters -= person_liters
        else:
            print(f'{people.popleft()} must wait') 
    else:
        _, liters_to_add = command.split()
        liters += int(liters_to_add)

    command = input()
print(f'{liters} liters left')