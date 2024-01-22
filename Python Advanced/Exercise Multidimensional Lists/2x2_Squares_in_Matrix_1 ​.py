rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for el in range(rows)]

equals_block = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol = matrix[row][col]

        if symbol == matrix[row][col] and symbol == matrix[row][col + 1] and symbol == matrix[row + 1][
            col] and symbol == matrix[row + 1][col + 1]:
            equals_block += 1

print(equals_block)