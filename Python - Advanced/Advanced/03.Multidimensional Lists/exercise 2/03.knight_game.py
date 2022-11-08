rows = int(input())
chess_board = [list(input()) for _ in range(rows)]

# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0

possible_moves = (
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    most_attacks_knight = []

    for row in range(rows):
        for col in range(rows):
            if chess_board[row][col] == 'K':
                attacks = 0

                for pos in possible_moves:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < rows and 0 <= pos_col < rows:
                        if chess_board[pos_row][pos_col] == 'K':
                            attacks += 1
                if attacks > max_attacks:
                    most_attacks_knight = [row, col]
                    max_attacks = attacks

    if most_attacks_knight:
        chess_board[most_attacks_knight[0]][most_attacks_knight[1]] = '0'
        removed_knights += 1
    else:
        break
print(removed_knights)