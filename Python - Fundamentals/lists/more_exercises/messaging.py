numbers = input().split()
text = input()

message = ""

for num in numbers:
    char_index = 0
    for digit in num:
        char_index += int(digit)
    if char_index > len(text):
        char_index -= len(text)
    message += text[char_index]
    text = text[:char_index] + text[char_index+1:]
print(message)