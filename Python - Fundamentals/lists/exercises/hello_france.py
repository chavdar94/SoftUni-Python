items_list = input().split("|")
budget = int(input())

bought_items = []
for item in items_list:
    current_item = item.split("->")
    if float(current_item[1]) <= budget:
        if current_item[0] == "Clothes" and float(current_item[1]) <= 50.00:
            budget -= float(current_item[1])
            bought_items.append(float(current_item[1]))
        elif current_item[0] == "Shoes" and float(current_item[1]) <= 35.00:
            budget -= float(current_item[1])
            bought_items.append(float(current_item[1]))
        elif current_item[0] == "Accessories" and float(current_item[1]) <= 20.50:
            budget -= float(current_item[1])
            bought_items.append(float(current_item[1]))


new_prices_list = []
for item_price in bought_items:
    new_price = item_price + (item_price * 0.40)
    new_prices_list.append(new_price)


for price in new_prices_list:
    print(f"{price:.2f}", end=" ")
print()
profit = sum(new_prices_list) - sum(bought_items)
print(f"Profit: {profit:.2f}")

if budget + sum(new_prices_list) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

