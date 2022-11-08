text = input()
for index, letter in enumerate(text):
    if ':' == letter:
        print(f'{letter}{text[index+1]}')