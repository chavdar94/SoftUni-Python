import re

name = r'%([A-Z][a-z]+)%'
product = r'<([\w]+)>'
quantity = r'\|(\d+)\|'
price = r'(\d+\.\d+)\b([$]){1}|(\d+\d+)\b([$]){1}'

total_income = 0
command = input()
while command != 'end of shift':
    p_name = re.search(name, command)
    p_product = re.search(product, command)
    p_quantity = re.search(quantity, command)
    p_price = re.search(price, command)

    if p_name is not None and p_product is not None and p_quantity is not None and p_price is not None:
        find_name, find_product, find_quantity, find_price = p_name[1], p_product[1], p_quantity[1], p_price[1]
        if find_price is None:
            find_price = p_price[3]

        current_price = int(find_quantity) * float(find_price)
        total_income += current_price
        print(f'{find_name}: {find_product} - {current_price:.2f}')
    command = input()
print(f'Total income: {total_income:.2f}')