import re

text = input()

pattern = r'([|#])([A-Za-z\s]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]+)\1'
matches = re.finditer(pattern, text)

foods = []
calories = 0

for match in matches:
    foods.append({'food': match.group(2), 'date': match.group(3), 'cals': match.group(4)})
    calories += int(match.group(4))

days = calories // 2000
print(f'You have food to last you for: {days} days!')
for item in foods:
    print(f"Item: {item['food']}, Best before: {item['date']}, Nutrition: {item['cals']}")