word = input()
capitalized = []
for i in range(len(word)):
    if word[i].isupper():
        capitalized.append(i)
print(capitalized)
