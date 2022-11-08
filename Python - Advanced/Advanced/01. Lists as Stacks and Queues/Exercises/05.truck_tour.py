from collections import deque

petrol_pumps = int(input())
pumps = deque()

#  adding fuel stations to the queue
for _ in range(petrol_pumps):
    pump_info = input().split()  # amount of petrol in liters and distance in kilometers
    pumps.append([int(x) for x in pump_info])

for i in range(petrol_pumps):
    total_fuel = 0
    failed_attempt = False
    for fuel, distance in pumps:
        total_fuel = total_fuel + fuel - distance
        if total_fuel < 0:
            failed_attempt = True
            break

    if failed_attempt:
        pumps.append(pumps.popleft())
    else:
        print(i)
        break
