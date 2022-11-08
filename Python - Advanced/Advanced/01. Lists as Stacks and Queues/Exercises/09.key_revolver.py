from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
value_of_intelligence = int(input())

bullets_counter = 0
barrel = 0

while bullets and locks:
    bullets_counter += 1
    barrel += 1
    current_bullet = bullets.pop()
    if current_bullet <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')

    if barrel == gun_barrel_size and bullets:
        print('Reloading!')
        barrel = 0
if not locks:
    money_earned = value_of_intelligence - (bullets_counter * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
