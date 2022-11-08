number_of_cars = int(input())

parking = {}

for car in range(number_of_cars):
    command = input().split()
    task = command[0]
    name = command[1]
    if task == 'register':
        license_plate = command[2]
        if name not in parking:
            parking[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[name]}")
    elif task == 'unregister':
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            del parking[name]
            print(f"{name} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")