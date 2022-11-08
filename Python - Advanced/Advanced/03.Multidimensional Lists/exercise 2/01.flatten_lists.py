data = input().split('|')
result = []
for i in range(len(data)-1, -1, -1):
    numbers = data[i].strip().split()
    result.extend(numbers)
print(' '.join(result))