import re

pattern = r'([=/])([A-Z][a-zA-Z]{2,})\1'

text = input()

destinations = []
score = 0
matches = re.finditer(pattern,text)
for match in matches:
    destinations.append(match.group(2))
    score += len(match.group(2))

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {score}')