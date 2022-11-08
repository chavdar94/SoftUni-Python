from collections import deque

seats = input().split(', ')
first = deque(int(x) for x in input().split(', '))
second = deque(int(x) for x in input().split(', '))

rotations = 0
matched_seats = []

while rotations < 10:
    rotations += 1

    first_num = first.popleft()
    second_num = second.pop()
    seat_char = chr(first_num + second_num)

    if f'{first_num}{seat_char}' in matched_seats or f'{second_num}{seat_char}' in matched_seats:
        continue

    if f'{first_num}{seat_char}' in seats:
        matched_seats.append(f'{first_num}{seat_char}')
    elif f'{second_num}{seat_char}' in seats:
        matched_seats.append(f'{second_num}{seat_char}')
    else:
        first.append(first_num)
        second.appendleft(second_num)

    if len(matched_seats) == 3:
        break

print(f'Seat matches: {", ".join(matched_seats)}')
print(f'Rotations count: {rotations}')