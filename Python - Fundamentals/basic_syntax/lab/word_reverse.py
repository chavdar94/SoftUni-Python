word = input()
reversed_word = ""
for ch in range(len(word)-1, -1, -1):
    reversed_word += word[ch]

print(reversed_word)