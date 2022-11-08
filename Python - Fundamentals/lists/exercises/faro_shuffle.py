cards = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    left_side = cards[:len(cards)//2]
    right_side = cards[len(cards)//2:]
    cards = []
    for card in range(len(left_side)):
        cards.append(left_side[card])
        cards.append(right_side[card])
print(cards)
