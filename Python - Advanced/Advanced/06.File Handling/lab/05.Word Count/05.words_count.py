import re


def read_words():
    with open('words.txt') as file:
        return file.read().split()


def count_words(words):
    words_count = {
        word: 0 for word in words
    }

    with open('text.txt') as file:
        for line in file:
            words_in_line = re.findall(r'\b\S+\b', line.lower())
            for word in words:
                words_count[word] += words_in_line.count(word)
    return words_count


def sort_result():
    return sorted(count_words(read_words()).items(), key=lambda x: -x[1])


def write_output():
    with open('output.txt', 'w') as file:
        for word, count in sort_result():
            file.write(f'{word} - {count}\n')


write_output()
