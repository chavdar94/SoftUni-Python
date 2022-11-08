key_words = input().split(', ')
text = input()

for word in key_words:
    text = text.replace(word, '*' * len(word))
print(text)
