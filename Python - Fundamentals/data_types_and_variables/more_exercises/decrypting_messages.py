key = int(input())
number_of_letters = int(input())

message = ""
for char in range(number_of_letters):
    letter = input()
    new_letter = ord(letter) + key
    message += chr(new_letter)
print(message)