number_of_elements = int(input())
unique_numbers = set()

for _ in range(number_of_elements):
    for el in input().split():
        unique_numbers.add(el)

print(*unique_numbers, sep="\n")