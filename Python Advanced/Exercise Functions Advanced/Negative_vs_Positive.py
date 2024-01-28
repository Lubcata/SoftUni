def number(*args):
    numbers_to_int = [int(x) for x in args]
    negative_numbers = 0
    positive_numbers = 0

    for num in numbers_to_int:
        if num < 0:
            negative_numbers += num
        else:
            positive_numbers += num

    print(negative_numbers)
    print(positive_numbers)

    if abs(negative_numbers) > positive_numbers:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


data = input().split()

number(*data)
