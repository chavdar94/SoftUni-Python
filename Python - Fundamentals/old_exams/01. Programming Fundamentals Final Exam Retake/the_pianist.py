def add_pieces(pieces_dict):
    current_piece = input().split('|')
    piece = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    pieces_dict[piece] = {'composer': composer, 'key': key}
    return pieces_dict


def add(pieces_dict, piece, composer, key):
    if piece in pieces_dict:
        print(f"{piece} is already in the collection!")
    else:
        pieces_dict[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    return pieces_dict


def remove(pieces_dict, piece):
    if piece in pieces_dict:
        del pieces_dict[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces_dict


def change_key(pieces_dict, piece, new_key):
    if piece in pieces_dict:
        pieces_dict[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces_dict


number_of_pieces = int(input())
pieces_dict = {}

for _ in range(number_of_pieces):
    add_pieces(pieces_dict)

while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split('|')
    current_command = command[0]
    piece = command[1]

    if current_command == 'Add':
        composer = command[2]
        key = command[3]
        add(pieces_dict, piece, composer, key)
    elif current_command == 'Remove':
        remove(pieces_dict, piece)
    elif current_command == 'ChangeKey':
        new_key = command[2]
        change_key(pieces_dict, piece, new_key)

for show in pieces_dict:
    print(f"{show} -> Composer: {pieces_dict[show]['composer']}, Key: {pieces_dict[show]['key']}")