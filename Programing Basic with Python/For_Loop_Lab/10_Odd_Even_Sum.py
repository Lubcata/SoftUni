count_of_numbers = int(input())
odd = 0
even = 0

for number in range(1, count_of_numbers + 1):
    current_number = int(input())
    if number % 2 == 0:
        odd += current_number
    else:
        even += current_number

difference = abs(odd - even)
if odd == even:
    print("Yes")
    print(f"Sum = {odd}")
else:
    print("No")
    print(f"Diff = {difference}")