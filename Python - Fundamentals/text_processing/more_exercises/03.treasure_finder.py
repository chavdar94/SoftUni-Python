secret_key = list(map(int, input().split()))
message = input()

key_len = len(secret_key)

while message != 'find':

    secret_text = []
    for i in range(len(message)):
        secret_text.append(chr(ord(message[i]) - secret_key[i % key_len]))

    secret_text = ''.join(secret_text)
    item = secret_text.split('&')[-2]
    location = secret_text.split('<')[-1][:-1]
    print(f'Found {item} at {location}')

    message = input()

