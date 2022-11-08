numbers = list(map(int, input().split(", ")))

even_indexes = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_indexes.append(i)
        
print(even_indexes)