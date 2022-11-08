words = input()

words_dict = {}
for ch in words:
    if ch not in words_dict:
        words_dict[ch] = 0
    words_dict[ch] += 1

sorted_chars = sorted(words_dict.items())
for pair in sorted_chars:
    char, count = pair
    print(f'{char}: {count} time/s')