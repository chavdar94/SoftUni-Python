import re

pattern = r'(?<=\s)([a-zA-Z0-9]+[\.\_\-a-zA-Z0-9]*@[a-z\-]+(\.[a-z\-]+)+)'

text = input()
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())

