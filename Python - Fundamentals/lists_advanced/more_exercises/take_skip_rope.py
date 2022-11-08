message = input()
split_message = [w for w in message]

numbers_in_message = []
chars_in_message = []

for ch in split_message:
    if ch.isdigit():
        numbers_in_message.append(int(ch))
    else:
        chars_in_message.append(ch)

take = [numbers_in_message[n] for n in range(len(numbers_in_message)) if n % 2 == 0]
skip = [numbers_in_message[n] for n in range(len(numbers_in_message)) if n % 2 != 0]

taken = []

for i in range(len(take)):
    taken += chars_in_message[:take[i]]
    del chars_in_message[:take[i]]
    del chars_in_message[:skip[i]]

print(''.join(taken))
