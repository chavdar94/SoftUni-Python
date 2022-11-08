orders = {}

while True:
    data = input().split(' ')
    if 'buy' in data:
        break
    product_name = data[0]
    price = float(data[1])
    quantity = int(data[2])
  
    if product_name not in orders:
        orders[product_name] = {'price':price,'quantity':quantity}
    else:
        if orders[product_name]['price'] != price:
            orders[product_name]['price'] = price
        orders[product_name]['quantity'] += quantity

for key, value in orders.items():
    print(f"{key} -> {(value['price']*value['quantity']):.2f}")