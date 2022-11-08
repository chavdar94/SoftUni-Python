wagons = int(input())

train = []
for wagon in range(wagons):
    train.append(0)


while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    task = command[0]

    if task == "add":
        add = int(command[1])
        train[-1] += add
    elif task == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif task == "leave":
        index = int(command[1])
        people = int(command[2])
        people_to_remove = train[index] - people
        train[index] = people_to_remove

print(train)