coffees = input().split(" ")
count_of_commands = int(input())

for current_coffee in range(count_of_commands):
    current_command = input().split(" ")
    my_command = current_command[0]
    if my_command == "Include":
        coffee_include = current_command[1]
        coffees.append(coffee_include)
    if my_command == "Remove":
        first_or_last = current_command[1]
        number_of_coffees = int(current_command[2])
        if number_of_coffees < len(coffees):
            if first_or_last == "first":
                coffees = coffees[number_of_coffees:]
            elif first_or_last == "last":
                coffees = coffees[:-number_of_coffees]
    if my_command == "Prefer":
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        if first_index < len(coffees) and second_index < len(coffees):
            coffees[first_index], coffees[second_index] = coffees[second_index], coffees[first_index]
    if my_command == "Reverse":
        coffees.reverse()

print("Coffees:")
print(" ".join(coffees))

