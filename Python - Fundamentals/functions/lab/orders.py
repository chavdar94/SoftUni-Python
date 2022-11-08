product = input()
quantity = int(input())

coffee = 1.5
water = 1.0
coke = 1.4
snacks = 2.0


def price(prod, qty):
    total_price = 0
    if prod == "coffee":
        total_price += coffee * qty
    elif prod == "water":
        total_price += water * qty
    elif prod == "coke":
        total_price += coke * qty
    elif prod == "snacks":
        total_price += snacks * qty
    return f"{total_price:.2f}"


print((price(product, quantity)))
