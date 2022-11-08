from collections import deque


def add_robots():
    result = {}
    robots_info = input().split(';')
    for robot in robots_info:
        name, processing_time = robot.split('-')
        result[name] = int(processing_time)
    return result


def to_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


def add_products():
    result = deque()
    while True:
        product = input()
        if product == 'End':
            break
        result.append(product)
    return result


def sec_to_hours(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = add_robots()
available_robots = [key for key in robots.keys()]
processing_robots = {}

starting_time = [int(x) for x in input().split(':')]
time_in_seconds = to_seconds(starting_time[0], starting_time[1], starting_time[2])
products = add_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)

    for robot_name in [key for key in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] == 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f'{robot_name} - {current_product} [{sec_to_hours(time_in_seconds)}]')
            processing_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(current_product)
