def shopping_cart(*args):
    products = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }
    result = ''
    flag = True

    for items in args:
        if items == 'Stop':
            break

        meal, product = items

        if meal == 'Soup' and len(products[meal]) < 3 and product not in products[meal]:
            products[meal].append(product)
        elif meal == 'Pizza' and len(products[meal]) < 4 and product not in products[meal]:
            products[meal].append(product)
        elif meal == 'Dessert' and len(products[meal]) < 2 and product not in products[meal]:
            products[meal].append(product)

    for key, value in sorted(products.items(), key=lambda x: (-len(x[-1]), x[0])):
        result += f'{key}:\n'
        for prod in sorted(value):
            result += f' - {prod}\n'

    if any(products.values()):
        return result
    else:
        return 'No products in the cart!'


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
