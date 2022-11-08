list_of_events = input().split("|")

total_energy = 100
total_coins = 100
is_open = True
for event in list_of_events:
    current_event = event.split("-")
    if current_event[0] == "rest":
        temp_energy = total_energy
        total_energy += int(current_event[1])
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - temp_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif current_event[0] == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += int(current_event[1])
            print(f"You earned {current_event[1]} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        if total_coins >= int(current_event[1]):
            total_coins -= int(current_event[1])
            print(f"You bought {current_event[0]}.")
        else:
            is_open = False
            print(f"Closed! Cannot afford {current_event[0]}.")
            break

if is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
