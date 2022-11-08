symbols_to_replace = {"-", ",", ".", "!", "?"}

with open('text.txt', 'r') as file:
    for line, text in enumerate(file):
        if line % 2 == 0:
            for element in symbols_to_replace:
                text = text.strip().replace(element, '@')
            text = text.split()
            print(*text[::-1])