import re

pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)+!(\d+)'

text = input()
furnitures = []
total_cost = 0
while text != 'Purchase':

    matches = re.search(pattern, text)
    if matches:
        furniture, price, quantity = matches.groups()
        furnitures.append(furniture)
        total_cost += float(price) * int(quantity)
    text = input()

print('Bought furniture:')
if furnitures:
    print('\n'.join(furnitures))
print(f'Total money spend: {total_cost:.2f}')