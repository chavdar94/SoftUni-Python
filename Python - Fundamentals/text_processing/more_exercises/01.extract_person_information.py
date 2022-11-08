number_of_lines = int(input())

for data in range(number_of_lines):
    text = input()
    name = text[text.index('@') + 1:text.index('|')]
    age = text[text.index('#') + 1:text.index('*')]
    print(f'{name} is {age} years old.')
