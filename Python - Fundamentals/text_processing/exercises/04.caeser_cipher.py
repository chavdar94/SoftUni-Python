word = input()
new_word = ''
for ch in word:
    new_word += chr(ord(ch) + 3)

print(new_word)