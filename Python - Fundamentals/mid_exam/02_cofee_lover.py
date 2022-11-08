coffee_names = input().split()
number_of_commands = int(input())

for coffee in range(number_of_commands):
    command = input().split()
    task = command[0]
    if task == "Include":
        coffee_names.append(command[1])
    elif task == "Remove":
        if 0 > int(command[2]) >= len(coffee_names):
            continue
        else:
            if command[1] == "first":
                del coffee_names[:int(command[2])]
            elif command[1] == "last":
                del coffee_names[-int(command[2]):]
    elif task == "Prefer":
        coffee_index_one = int(command[1])
        coffee_index_two = int(command[2])
        if 0 <= coffee_index_one < len(coffee_names) and 0 <= coffee_index_two < len(coffee_names):
            coffee_names[coffee_index_one], coffee_names[coffee_index_two] = coffee_names[coffee_index_two], \
                                                                             coffee_names[coffee_index_one]
        else:
            continue
    elif task == "Reverse":
        coffee_names.reverse()

print("Coffees:")
print(" ".join(coffee_names))
