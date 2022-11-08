from collections import deque

milligrams_caffeine = list(map(int, input().split(', ')))
energy_drinks = deque(int(x) for x in input().split(', '))

night_caffeine = 0

while milligrams_caffeine and energy_drinks:
    last_caffeine = milligrams_caffeine.pop()
    first_drink = energy_drinks.popleft()

    current_caffeine = last_caffeine * first_drink
    if night_caffeine + current_caffeine > 300:
        energy_drinks.append(first_drink)
        night_caffeine -= 30
        if night_caffeine < 0:
            night_caffeine = 0
    else:
        night_caffeine += current_caffeine

if energy_drinks:
    print(f'Drinks left: {", ".join(str(x) for x in energy_drinks)}')
else:
    print('At least Stamat wasn\'t exceeding the maximum caffeine.')
print(f"Stamat is going to sleep with {night_caffeine} mg caffeine.")