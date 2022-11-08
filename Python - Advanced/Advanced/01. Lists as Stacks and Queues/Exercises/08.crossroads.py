from collections import deque

green_light = int(input())
window = int(input())

cars = deque()
cars_passed = 0
crashed = False

while True:
    command = input()
    if command == 'END':
        break

    if command == 'green':
        if cars:
            current_car = cars.popleft()
            seconds_left = green_light - len(current_car)
            while seconds_left > 0:
                cars_passed += 1
                if cars:
                    current_car = cars.popleft()
                    seconds_left -= len(current_car)
                else:
                    break
            if seconds_left == 0:
                cars_passed += 1
            elif window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_passed += 1
            else:
                idx = window + seconds_left
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[idx]}.")
                crashed = True
                break
    else:
        cars.append(command)

if not crashed:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
