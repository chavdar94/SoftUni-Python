def add_stop(destinations, index, string):
    if 0 <= index < len(destinations):
        destinations = destinations[:index] + string + destinations[index:]
    return destinations


def remove_stop(destinations, start_index, end_index):
    if 0 <= start_index < len(destinations) and 0 <= end_index < len(destinations):
        destinations = destinations[:start_index] + destinations[end_index + 1:]
    return destinations


def switch(destinations, old_string, new_string):
    if old_string in destinations:
        destinations = destinations.replace(old_string, new_string)
    return destinations


stops = input()
while True:
    command = input()
    if command == 'Travel':
        break
    command = command.split(':')
    current_command = command[0]

    if current_command == 'Add Stop':
        index = int(command[1])
        string = command[2]
        stops = add_stop(stops, index, string)
    elif current_command == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        stops = remove_stop(stops, start_index, end_index)
    elif current_command == 'Switch':
        old_string = command[1]
        new_string = command[2]
        stops = switch(stops, old_string, new_string)
    print(stops)
print(f'Ready for world tour! Planned stops: {stops}')
