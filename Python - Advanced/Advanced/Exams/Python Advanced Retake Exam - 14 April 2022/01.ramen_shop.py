from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while bowls_of_ramen and customers:
    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()

    if bowl > customer:
        bowl -= customer
        bowls_of_ramen.append(bowl)

    elif customer > bowl:
        customer -= bowl
        customers.appendleft(customer)

if not customers:
    print('Great job! You served all the customers.')
    if bowls_of_ramen:
        print(f'Bowls of ramen left: {", ".join(str(s) for s in bowls_of_ramen)}')

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join(str(s) for s in customers)}')