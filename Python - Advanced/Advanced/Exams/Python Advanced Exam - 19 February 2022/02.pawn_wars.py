def check_diagonal(pawn):
    if pawn == 'White':
        if (0 <= white_pos[0] - 1 < SIZE and 0 <= white_pos[1] - 1 < SIZE and
            chessboard[white_pos[0] - 1][white_pos[1]-1] == 'b')\
                or (0 <= white_pos[0] -1 < SIZE and 0 <= white_pos[1] + 1 < SIZE and
                    chessboard[white_pos[0] - 1][white_pos[1]+1] == 'b'):
            print(f'Game over! White win, capture on {col_char[black_pos[1]]}{SIZE - black_pos[0]}.')
            return True

    elif pawn == 'Black':
        if (0 <= black_pos[0] + 1 < SIZE and 0 <= black_pos[1] - 1 < SIZE and
            chessboard[black_pos[0] + 1][black_pos[1] - 1] == 'w') \
                or (0 <= black_pos[0] + 1 < SIZE and 0 <= black_pos[1] + 1 < SIZE and
                    chessboard[black_pos[0] + 1][black_pos[1] + 1] == 'w'):
            print(f'Game over! Black win, capture on {col_char[white_pos[1]]}{SIZE - white_pos[0]}.')
            return True

    return False


def get_pos(pawn, coords):
    n_row, n_col = 0, ''
    if pawn == 'White':
        n_row = SIZE - coords[0]
        n_col = col_char[coords[1]]
    elif pawn == 'Black':
        n_row = SIZE - coords[0]
        n_col = col_char[coords[1]]

    return f'{n_col}{n_row}'


SIZE = 8

col_char = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'
}

chessboard = []

white_pos = []
black_pos = []

for row in range(SIZE):
    line = input().split()
    if 'w' in line:
        white_pos = [row, line.index('w')]

    if 'b' in line:
        black_pos = [row, line.index('b')]

    chessboard.append(line)

pawns = ['White', 'Black']

while True:

    pawn_turn = pawns.pop(0)

    if check_diagonal(pawn_turn):
        break

    if pawn_turn == 'White':
        if white_pos[0] == 0:
            print(f'Game over! {pawn_turn} pawn is promoted to a queen at {get_pos(pawn_turn, white_pos)}.')
            break
        chessboard[white_pos[0]][white_pos[1]] = '-'
        chessboard[white_pos[0] - 1][white_pos[1]] = 'w'
        white_pos[0] -= 1

    elif pawn_turn == 'Black':
        if black_pos[0] == SIZE - 1:
            print(f'Game over! {pawn_turn} pawn is promoted to a queen at {get_pos(pawn_turn, black_pos)}.')
            break
        chessboard[black_pos[0]][black_pos[1]] = '-'
        chessboard[black_pos[0] + 1][black_pos[1]] = 'b'
        black_pos[0] += 1

    pawns.append(pawn_turn)