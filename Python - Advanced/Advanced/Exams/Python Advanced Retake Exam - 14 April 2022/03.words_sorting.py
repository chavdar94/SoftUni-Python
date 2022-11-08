def words_sorting(*args):
    words = {}
    result = ''

    for word in args:
        if word not in words:
            words[word] = sum(ord(x) for x in word)
    sum_values = 0
    for val in words.values():
        sum_values += val

    if sum_values % 2 == 0:
        for k, v in sorted(words.items()):
            result += f'{k} - {v}\n'

    else:
        for k, v in sorted(words.items(), key=lambda x: -x[1]):
            result += f'{k} - {v}\n'

    return result


print(
    words_sorting(
        'cacophony',
        'accolade'
  ))


