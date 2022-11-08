name_of_gifts = input().split()

while True:
    command = input()
    command_list = command.split()
    if "No Money" in command:
        break
    if "OutOfStock" in command_list:
        for i in range(len(name_of_gifts)):
            if name_of_gifts[i] == command_list[-1]:
                name_of_gifts[i] = "None"
    elif "Required" in command_list:
        for j in range(len(name_of_gifts)):
            if j == int(command_list[-1]):
                name_of_gifts[j] = command_list[1]
    elif "JustInCase" in command_list:
        name_of_gifts[-1] = command_list[-1]

for gift in range(len(name_of_gifts)):
    if "None" in name_of_gifts:
        name_of_gifts.remove("None")
print(" ".join(name_of_gifts))