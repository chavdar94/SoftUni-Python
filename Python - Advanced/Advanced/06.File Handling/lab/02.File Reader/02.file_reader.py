with open('numbers.txt', 'r') as numbers_file:
    result = 0
    for line in numbers_file:
        result += int(line)
    print(result)