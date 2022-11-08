numbers = [int(x) for x in input().split()]

inverted_numbers = [-abs(x) if x > 0 else abs(x) for x in numbers]

print(inverted_numbers)

