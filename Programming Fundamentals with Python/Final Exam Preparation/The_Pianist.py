def add(pieces, curr_piece, curr_composer, curr_key):
    if curr_piece in pieces.keys():
        print(f"{curr_piece} is already in the collection!")
    else:
        pieces[curr_piece] = {"composer": curr_composer, "key": curr_key}
        print(f"{curr_piece} by {curr_composer} in {curr_key} added to the collection!")
    return pieces


def remove(pieces, curr_piece):
    if curr_piece in pieces.keys():
        pieces.pop(curr_piece)
        print(f"Successfully removed {curr_piece}!")
    else:
        print(f"Invalid operation! {curr_piece} does not exist in the collection.")
    return pieces


def change_key(pieces, curr_piece, new_key):
    if curr_piece in pieces:
        pieces[curr_piece]["key"] = new_key
        print(f"Changed the key of {curr_piece} to {new_key}!")
    else:
        print(f"Invalid operation! {curr_piece} does not exist in the collection.")
    return pieces


def main():
    number_of_pieces = int(input())
    pieces = {}
    for number in range(number_of_pieces):
        piece_info = input().split("|")
        piece = piece_info[0]
        composer = piece_info[1]
        key = piece_info[2]
        pieces[piece] = {"composer": composer, "key": key}
    while True:
        command = input().split("|")
        action = command[0]
        if action == "Stop":
            break
        curr_piece = command[1]

        if action == "Add":
            curr_composer = command[2]
            curr_key = command[3]

            add(pieces, curr_piece, curr_composer, curr_key)
        elif action == "Remove":
            remove(pieces, curr_piece)
        elif action == "ChangeKey":
            # "ChangeKey|{piece}|{new key}":
            new_key = command[2]
            change_key(pieces, curr_piece, new_key)
    for piece, pieces_info in pieces.items():
        print(f"{piece} -> Composer: {pieces_info['composer']}, Key: {pieces_info['key']}")


main()
