import re

patter = r'\d+'

while True:
    text = input()
    if text:
        result = re.finditer(patter, text)

        for match in result:
            print(match.group(), end=' ')
    else:
        break

