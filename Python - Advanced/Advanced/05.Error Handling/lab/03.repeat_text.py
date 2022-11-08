try:
    text = input()
    repetitions = int(input())
    result = text * repetitions
    print(result)
except ValueError:
    print('Variable times must be an integer')
