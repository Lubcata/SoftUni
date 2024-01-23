rows, cols = [int(x) for x in input().split(", ")]
matrix = []

sum_of_matrix = 0
for row in range(rows):
    elements = [int(el) for el in input().split(", ")]
    matrix.append(elements)
    sum_of_matrix += sum(elements)


print(sum_of_matrix)
print(matrix)
