def insert_space(text, idx):
    text = text[:idx] + ' ' + text[idx:]
    print(text)
    return text


def reverse(text, substr):
    if substr in text:
        substr_index = text.index(substr)
        substr_len = len(substr)
        text = text[:substr_index] + text[substr_index + substr_len:] + substr[::-1]
        print(text)
    else:
        print('error')
    return text


def change_all(text, substr, replace):
    text = text.replace(substr, replace)
    print(text)
    return text


message = input()
command = input()
while command != 'Reveal':
    command = command.split(':|:')
    current_command = command[0]
    if current_command == 'InsertSpace':
        index = int(command[1])
        message = insert_space(message, index)
    elif current_command == 'Reverse':
        substring = command[1]
        message = reverse(message, substring)
    elif current_command == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)
    command = input()
print(f'You have a new text message: {message}')