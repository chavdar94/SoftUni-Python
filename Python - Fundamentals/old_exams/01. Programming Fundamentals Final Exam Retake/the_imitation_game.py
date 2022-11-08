def move(text, number, ):
    new_text = text[number:] + text[:number]
    return new_text


def insert(text, idx, val):
    if idx < len(text):
        for index, value in enumerate(text):
            if index == idx:
                text = text[:index] + val + text[index:]
    else:
        text += val
    return text



def change(text, subs, replace):
    text = text.replace(subs, replace)
    return text


encrypted_message = input()
decrypted_message = ''

while True:
    message = input()
    if message == 'Decode':
        break
    message = message.split('|')
    if 'Move' in message:
        number_of_letters = int(message[1])
        decrypted_message = move(encrypted_message, number_of_letters)

    elif 'Insert' in message:
        index = int(message[1])
        value = message[2]
        decrypted_message = insert(encrypted_message, index, value)

    elif 'ChangeAll' in message:
        substring = message[1]
        replacement = message[2]
        decrypted_message = change(encrypted_message, substring, replacement)

    encrypted_message = decrypted_message

print(f'The decrypted message is: {decrypted_message}')
