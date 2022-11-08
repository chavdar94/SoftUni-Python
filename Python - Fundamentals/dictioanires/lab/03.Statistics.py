bakery = {}

while True:
    products = input().split(': ')
    if 'statistics' in products:
        break
    
    key = products[0]
    value = int(products[1])
    if key not in bakery:
        bakery[key] = 0
    bakery[key] += value

print('Products in stock:')
for key,value in bakery.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(bakery.keys())}')
print(f'Total Quantity: {sum(bakery.values())}')

