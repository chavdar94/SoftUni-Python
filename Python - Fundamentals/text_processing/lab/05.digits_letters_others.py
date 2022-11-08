def get_digits(word):
    return ''.join([char for char in word if char.isdigit()])


def get_letters(word):
    return ''.join([char for char in word if char.isalpha()])


def get_others(word):
    return ''.join([char for char in word if not char.isalnum()])


word = input()
print(get_digits(word))
print(get_letters(word))
print(get_others(word))
