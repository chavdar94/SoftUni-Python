def check_index(key, start_index, end_index):
    if 0 <= start_index < len(key) and 0 <= end_index < len(key):
        return True
    return False


def contains(key, substr):
    if substr in key:
        print(f"{key} contains {substr}")
    else:
        print("Substring not found!")
    return key


def flip(key, task, start_index, end_index):
    if check_index(key, start_index, end_index):
        sliced = key[start_index:end_index]
        if task == 'Upper':
            upped = sliced.upper()
            key = key.replace(sliced, upped)
        elif task == 'Lower':
            lowered = sliced.lower()
            key = key.replace(sliced, lowered)
        print(key)
        return key


def slice_func(key, start_index, end_index):
    if check_index(key, start_index, end_index):
        key = key[:start_index] + key[end_index:]
    print(key)
    return key


raw_key = input()
command = input()
while command != 'Generate':
    command = command.split('>>>')
    current_command = command[0]

    if current_command == 'Contains':
        substring = command[1]
        raw_key = contains(raw_key, substring)

    elif current_command == 'Flip':
        task = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        raw_key = flip(raw_key, task, start_index, end_index)

    elif current_command == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        raw_key = slice_func(raw_key, start_index, end_index)

    command = input()
print(f'Your activation key is: {raw_key}')