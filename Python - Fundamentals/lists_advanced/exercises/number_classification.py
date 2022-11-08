numbers = list(map(int, input().split(", ")))
positives = [str(x) for x in numbers if x >= 0]
negatives = [str(x) for x in numbers if x < 0]
evens = [str(x) for x in numbers if x % 2 == 0]
odds = [str(x) for x in numbers if x % 2 != 0]

print(f'Positive: {", ".join(positives)}')
print(f'Negative: {", ".join(negatives)}')
print(f'Even: {", ".join(evens)}')
print(f'Odd: {", ".join(odds)}')
