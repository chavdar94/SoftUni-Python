from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

wasted_water = 0
cups_filled = 0

while cups and bottles:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()
    cups_filled += 1

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup

    elif current_bottle < current_cup:
        current_cup -= current_bottle
        while current_cup > 0:
            current_bottle = bottles.pop()
            current_cup -= current_bottle
            if current_cup <= 0:
                wasted_water += abs(current_cup)
                break

if not cups:
    bottles_left = list(map(str, bottles))
    print(f'Bottles: {" ".join(bottles_left)}')
elif not bottles:
    left_cups = list(map(str, [cup for cup in cups]))
    print(f'Cups: {" ".join(left_cups)}')

print(f'Wasted litters of water: {wasted_water}')
