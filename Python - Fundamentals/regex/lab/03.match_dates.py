import re

pattern = r'\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b'
dates = input()
matches = re.finditer(pattern, dates)

for match in matches:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')