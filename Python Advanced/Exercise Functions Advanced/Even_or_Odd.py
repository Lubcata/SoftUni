def even_odd(*args):
    *numbers, command = args
    if command == "even":
        result = [el for el in numbers if el % 2 == 0]
        return result
    elif command == "odd":
        result = [el for el in numbers if el % 2 != 0]
        return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
