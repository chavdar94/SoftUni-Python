text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

no_vowels = [x for x in text if x not in vowels]
print(''.join(no_vowels))
