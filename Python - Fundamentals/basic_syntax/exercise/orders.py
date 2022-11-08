orders = int(input())

total = 0
for order in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days not in range(1, 32):
        continue
    elif capsule_count not in range(1,2001):
        continue
    current_price = price_per_capsule * days * capsule_count
    total += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")

print(f"Total: ${total:.2f}")
