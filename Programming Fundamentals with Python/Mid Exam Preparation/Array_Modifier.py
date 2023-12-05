def swap(numbers, first_index, second_index):
    numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]
    return numbers


def multiply(numbers, first_index, second_index):
    numbers[first_index] = numbers[first_index] * numbers[second_index]
    return numbers


def decrease(numbers):
    for curr_index in range(len(numbers)):
        numbers[curr_index] -= 1


def main():
    numbers = [int(number) for number in input().split()]
    while True:
        command = input().split()
        action = command[0]
        if action == "end":
            break
        if action == "swap":
            first_index = int(command[1])
            second_index = int(command[2])
            swap(numbers, first_index, second_index)
        elif action == "multiply":
            first_index = int(command[1])
            second_index = int(command[2])
            multiply(numbers, first_index, second_index)
        elif action == "decrease":
            decrease(numbers)
    numbers_str = [str(num) for num in numbers]
    print(", ".join(numbers_str))

main()
