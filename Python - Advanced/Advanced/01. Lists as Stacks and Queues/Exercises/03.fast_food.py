from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))
while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        orders.appendleft(current_order)
        print(f'Orders left: {" ".join(map(str, orders))}')
        break
else:
    print('Orders complete')