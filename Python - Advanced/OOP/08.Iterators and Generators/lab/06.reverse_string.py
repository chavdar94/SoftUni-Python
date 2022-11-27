def reverse_text(word):
    index = len(word) - 1

    while index >= 0:
        yield word[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
