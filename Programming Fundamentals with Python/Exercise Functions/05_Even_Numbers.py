def is_even(number):
    return number % 2 == 0

number_as_string = input().split()
number_as_digit = []

for number in number_as_string:
    number_as_digit.append(int(number))
even_number = []

for element in number_as_digit:
    if is_even(element):
        even_number.append(element)
print(even_number)
