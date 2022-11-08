import re

pattern = r'([@#])(?P<word>[a-zA-Z]{3,})\1\1(?P<word2>[a-zA-Z]{3,})\1'

text = input()
matches = list(re.finditer(pattern, text))
words = []

for pair in matches:
    if pair['word'] == pair['word2'][::-1]:
        words.append(f"{pair['word']} <=> {pair['word2']}")

if matches:
    print(f"{len(matches)} word pairs found!")
    if words:
        print("The mirror words are:")
        print(', '.join(words))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")