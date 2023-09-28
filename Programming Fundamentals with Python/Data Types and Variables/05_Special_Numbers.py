range_number = int(input())
for number in range(1, range_number + 1):
    number_string = str(number)
    status = False
    sum_numbers = 0
    for character in number_string:
        sum_numbers += int(character)
    if sum_numbers in [5, 7, 11]:
        status = True
    print(f"{number} -> {status}")