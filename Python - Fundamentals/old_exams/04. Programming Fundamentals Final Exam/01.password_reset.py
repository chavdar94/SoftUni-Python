def take_odd(password):
    password = ''.join([password[s] for s in range(len(password)) if s % 2 != 0])
    print(password)
    return password


def cut(password, index, length):
    if 0 <= index < len(password):
        password = password[:index] + password[index + length:]
        print(password)
        return password


def substitute_func(password, substring, substitute):
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
    else:
        print('Nothing to replace!')
    return password

password = input()
command = input()
while command != 'Done':
    command = command.split()
    current_command = command[0]
    if current_command == 'TakeOdd':
        password = take_odd(password)
    elif current_command == 'Cut':
        index = int(command[1])
        length = int(command[2])
        password = cut(password, index, length)
    elif current_command == 'Substitute':
        substring = command[1]
        substitute = command[2]
        password = substitute_func(password, substring, substitute)

    command = input()
print(f'Your password is: {password}')