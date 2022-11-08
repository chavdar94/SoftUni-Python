number_of_guests = int(input())

guests_codes = set()

for _ in range(number_of_guests):
    guest = input()
    guests_codes.add(guest)

while True:
    attending_guest = input()
    if attending_guest == 'END':
        break
    guests_codes.remove(attending_guest)

print(len(guests_codes))
sorted_guests = sorted(guests_codes)
for guest in sorted_guests:
    print(guest)