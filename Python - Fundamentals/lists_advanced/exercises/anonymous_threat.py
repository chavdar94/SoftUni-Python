data = input().split()

while True:
    command = input()
    if command == "3:1":
        break
    command = command.split()
    task = command[0]
    if task == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        #  if starting index is negative number
        if start_index < 0:
            start_index = 0
        # concatenating the strings in the given range (start_index:end_index)
        data[start_index:end_index + 1] = [''.join(data[start_index:end_index + 1])]

    elif task == "divide":
        index = int(command[1])
        partitions = int(command[2])
        # the string that will be divided
        divide = data[index]
        if 0 < partitions <= 100:
            data.pop(index)
            # number of pieces the string will be divided to
            chunks = len(divide) // partitions
            divide = [divide[i:i + chunks] for i in range(0, len(divide), chunks)]
            # if the string cannot be divided in equal parts, concatenating the last two parts into a single one
            if len(divide) % partitions != 0:
                divide[partitions - 1:len(divide)] = [''.join(divide[partitions - 1:len(divide)])]
            for i in range(len(divide)):
                data.insert(i + index, divide[i])

print(*data)
