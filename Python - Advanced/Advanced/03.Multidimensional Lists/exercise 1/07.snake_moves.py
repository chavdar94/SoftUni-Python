from collections import deque
rows, cols = [int(x) for x in input().split()]
word = deque(list(input()))

for row in range(rows):
    new_word = ''
    for col in range(cols):
        char = word.popleft()
        new_word += char
        word.append(char)
    if row % 2 == 0:
        print(new_word)
    else:
        print(new_word[::-1])
