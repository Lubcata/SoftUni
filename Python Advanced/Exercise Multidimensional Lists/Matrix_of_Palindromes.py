rows, cols = [int(el) for el in input().split()]
matrix = []

first_element = ord("a")

for row in range(first_element, first_element + rows):
    for col in range(row, row + cols):
        print(chr(row), chr(col), chr(row), sep="", end=" ")

    print()
