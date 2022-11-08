numbers = list(map(int,input().split()))
removed_pokemons = []
while len(numbers) > 0:
    index = int(input())
    removed = 0
    if 0 <= index < len(numbers):
        removed = numbers.pop(index)
    elif 0 > index:
        removed = numbers[0]
        numbers[0] = numbers[-1]
    else:
        removed = numbers[-1]
        numbers[-1] = numbers[0]
    removed_pokemons.append(removed)
    for i in range(len(numbers)):
        if numbers[i] <= removed:
            numbers[i] += removed
        else:
            numbers[i] -= removed
print(sum(removed_pokemons))