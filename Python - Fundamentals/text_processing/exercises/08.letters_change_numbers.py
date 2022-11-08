data = input().split()

total_sum = 0
for text in data:
    number = text[1:-1]
    current_sum = 0

    current_sum = int(number)
    if text[0].isupper():
        letter_position = ord(text[0]) - 64
        current_sum = current_sum / letter_position

    elif text[0].islower():
        letter_position = ord(text[0]) - 96
        current_sum = current_sum * letter_position

    if text[-1].isupper():
        letter_position = ord(text[-1]) - 64
        current_sum = current_sum - letter_position

    elif text[-1].islower():
        letter_position = ord(text[-1]) - 96
        current_sum = current_sum + letter_position

    total_sum += current_sum
    current_sum = 0

print(f"{total_sum:.2f}")
