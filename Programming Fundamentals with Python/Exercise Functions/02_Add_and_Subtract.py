def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    pass

def add_and_subtract(first, second, third):
    sum_of_first_and_second = sum_numbers(first, second)


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))