times = input().split()

left_racer = times[:len(times)//2]
right_racer = times[0-len(times)//2:]
right_racer.reverse()

left_racer_time = 0
right_racer_time = 0

for left_time in left_racer:
    if left_time == "0":
        left_racer_time *= 0.8
    left_racer_time += int(left_time)

for right_time in right_racer:
    if right_time == "0":
        right_racer_time *= 0.8
    right_racer_time += int(right_time)

if left_racer_time <= right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")