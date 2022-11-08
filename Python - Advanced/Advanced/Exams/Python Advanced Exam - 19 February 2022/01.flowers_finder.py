from collections import deque


def check_letter(letter):
    for word, char in key_words.items():
        try:
            key_words[word] = char.replace(letter, '')
        except TypeError:
            pass
        if not key_words[word]:
            found_word['found'] = True
            found_word['word'] = word
            break


vowels = deque(input().split())
consonants = input().split()

key_words = {'rose': 'rose',
             'tulip': 'tulip',
             'lotus': 'lotus',
             'daffodil': 'daffodil'}

found_word = {
    'found': False,
    'word': ''
}

while vowels and consonants and not found_word['found']:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    check_letter(vowel)
    check_letter(consonant)

if not found_word['found']:
    print('Cannot find any word!')
else:
    print(f"Word found: {found_word['word']}")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
