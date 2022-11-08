information = input()
phonebook = {}


while '-' in information:
    person_info = information.split('-')
    name = person_info[0]
    number = person_info[1]
    if name not in phonebook:
        phonebook[name] = number
    phonebook[name] = number

    information = input()


for person in range(int(information)):
    current_person = input()
    if current_person in phonebook:
        print(f'{current_person} -> {phonebook[current_person]}')
    else:
        print(f'Contact {current_person} does not exist.')