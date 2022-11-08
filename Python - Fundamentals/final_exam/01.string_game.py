def change(text, char, replacement):
    text = text.replace(char, replacement)
    print(text)
    return text


def includes(text, substring):
    if substring in text:
        print('True')
    else:
        print('False')


def end(text, substring):
    if text.endswith(substring):
        print('True')
    else:
        print('False')


def uppercase(text):
    text = text.upper()
    print(text)
    return text


def find_index(text, char):
    if char in text:
        result = text.index(char)
        print(result)


def cut(text, start_index, count):
    text = text[start_index:start_index+count]
    print(text)
    return text


text = input()
command = input()
while command != 'Done':

    command = command.split()
    current_command = command[0]

    if current_command == 'Change':
        char = command[1]
        replacement = command[2]
        text = change(text, char, replacement)

    elif current_command == 'Includes':
        substring = command[1]
        includes(text, substring)

    elif current_command == 'End':
        substring = command[1]
        end(text, substring)

    elif current_command == 'Uppercase':
        text = uppercase(text)

    elif current_command == 'FindIndex':
        char = command[1]
        find_index(text, char)

    elif current_command == 'Cut':
        start_index = int(command[1])
        count = int(command[2])
        cut(text, start_index, count)

    command = input()
