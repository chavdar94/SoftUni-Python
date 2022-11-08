word = input()

for index, value in enumerate(range(len(word)-1),1):
    if word[value] != word[index]:
        print(word[value], end='')
print(word[-1])