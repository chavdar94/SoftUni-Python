key_word = input()
word = input()
while key_word in word:
    word = word.replace(key_word, '')
print(word)