def add_car(cars_dict):
    current_car = input().split('|')
    car_model = current_car[0]
    mileage = int(current_car[1])
    fuel = int(current_car[2])
    cars_dict[car_model] = {'Mileage': mileage, 'Fuel': fuel}
    return cars_dict


def drive(cars_dict, car, distance, fuel):
    if car in cars_dict:
        if cars_dict[car]['Fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]['Mileage'] += distance
            cars_dict[car]['Fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car]['Mileage'] >= 100000:
                del cars_dict[car]
                print(f"Time to sell the {car}!")

    return cars_dict


def refuel(cars_dict, car, fuel):
    if cars_dict[car]['Fuel'] + fuel > 75:
        fuel = 75 - cars_dict[car]['Fuel']
        cars_dict[car]['Fuel'] = 75
    else:
        cars_dict[car]['Fuel'] += fuel
    print(f"{car} refueled with {fuel} liters")
    return cars_dict


def revert(cars_dict, car, distance):
    if cars_dict[car]['Mileage'] - distance < 10000:
        cars_dict[car]['Mileage'] = 10000
    else:
        cars_dict[car]['Mileage'] -= distance
        print(f"{car} mileage decreased by {distance} kilometers")
    return cars_dict


def show_info(cars_dict):
    for car in cars_dict:
        print(f"{car} -> Mileage: {cars_dict[car]['Mileage']} kms, Fuel in the tank: {cars_dict[car]['Fuel']} lt.")


number_of_cars = int(input())
cars = {}
for car in range(number_of_cars):
    add_car(cars)

command = input()
while command != 'Stop':

    command = command.split(' : ')
    current_command = command[0]
    current_car = command[1]
    if current_command == 'Drive':
        distance = int(command[2])
        fuel = int(command[3])
        drive(cars, current_car, distance, fuel)
    elif current_command == 'Refuel':
        fuel = int(command[2])
        refuel(cars, current_car, fuel)
    elif current_command == 'Revert':
        kilometers = int(command[2])
        revert(cars, current_car, kilometers)

    command = input()

show_info(cars)