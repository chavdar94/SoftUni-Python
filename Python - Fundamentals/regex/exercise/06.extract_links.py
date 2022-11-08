import re

pattern = r'((w{3})\.[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*(\.[a-z]+)+)'

text = input()
websites = []
while text:
    matches = re.search(pattern, text)
    if matches:
        websites.append(matches.group())

    text = input()
print('\n'.join(websites))