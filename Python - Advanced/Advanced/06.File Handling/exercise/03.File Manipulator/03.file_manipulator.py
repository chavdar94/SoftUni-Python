import os

while True:
    command = input().split('-')
    current_command = command[0]

    if current_command == 'End':
        break
    file_name = ''
    if len(command) > 1:
        file_name = command[1]
    if current_command == 'Create':
        file = open(f'./{file_name}', 'w')
        file.close()

    elif current_command == 'Add':
        content = command[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(f'{content}\n')

    elif current_command == 'Replace':
        old_string, new_string = command[2:]
        try:
            with open(f'./{file_name}', 'r+') as file:
                file_info = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate(0)
                file.write(file_info)
        except FileNotFoundError:
            print("An error occurred")

    elif current_command == 'Delete':
        try:
            os.remove(f'./{file_name}')
        except FileNotFoundError:
            print('An error occurred')