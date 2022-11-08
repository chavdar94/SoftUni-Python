import os

try:
    path = 'my_first_file.txt'
    os.remove(path)
except FileNotFoundError:
    print('File already deleted')