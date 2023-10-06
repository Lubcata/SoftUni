def is_palindrome(some_number_as_string: str) -> bool:
    return some_number_as_string == some_number_as_string[::-1]


numbers_as_string = input().split(", ")

for numbers_as_string in numbers_as_string:
    print(is_palindrome(numbers_as_string))

