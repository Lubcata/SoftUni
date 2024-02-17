def print_board(airspace):
    for row in airspace:
        print(''.join(row))


n = int(input())

armor_value = 300
enemies = 0

matrix = []
position = None

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row_index in range(n):
    data = list(input())

    if "J" in data:
        col_index = data.index("J")
        position = [row_index, col_index]

    for symbol in data:
        if symbol == "E":
            col_index = data.index("E")
            enemies += 1

    matrix.append(data)


while armor_value and enemies:
    direction = input()

    current_row_index, current_col_index = position
    row_movement, col_movement = direction_mapper[direction]
    next_row_index = current_row_index + row_movement
    next_col_index = current_col_index + col_movement

    symbol = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = "J"
    matrix[current_row_index][current_col_index] = "-"
    position = [next_row_index, next_col_index]

    if symbol == "E":
        enemies -= 1
        if enemies:
            armor_value -= 100
            if not armor_value:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{', '.join(str(el) for el in position)}]!")
                print_board(matrix)
                exit()
        else:
            print("Mission accomplished, you neutralized the aerial threat!")
            print_board(matrix)
            exit()
    if symbol == "R":
        armor_value = 300




