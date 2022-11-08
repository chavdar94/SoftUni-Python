from collections import deque

customers = deque()

while True:
    name = input()
    if name == 'End':
        print(f"{len(customers)} people remaining.")
        break
    elif name == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(name)