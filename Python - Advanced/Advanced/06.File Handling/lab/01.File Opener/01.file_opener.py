path = 'text.txt'

try:
    with open(path) as text_file:
        print('File found')
except FileNotFoundError:
    print('File not found')