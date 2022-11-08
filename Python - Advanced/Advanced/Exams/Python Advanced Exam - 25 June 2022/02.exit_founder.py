names = input().split(', ')

matrix = [input().split() for _ in range(6)]

skip_turn = False
skips = {
    'Tom': False,
    'Jerry': False
}

while True:
    player = names.pop(0)
    coordinates = [int(x) for x in input()[1:-1].split(',')]
    if skips[player]:
        names.append(player)
        skips[player] = False
        continue

    row, col = coordinates

    if matrix[row][col] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break

    elif matrix[row][col] == 'T':
        print(f"{player} is out of the game! The winner is {names[0]}.")
        break

    elif matrix[row][col] == 'W':
        print(f"{player} hits a wall and needs to rest.")
        skips[player] = True

    names.append(player)
