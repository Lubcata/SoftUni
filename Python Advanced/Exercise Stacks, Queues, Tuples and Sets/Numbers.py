first_set = {int(num) for num in input().split()}
second_set = {int(num) for num in input().split()}

functions = {
    "Add First": lambda x: [first_set.add(int(el)) for el in x],
    "Add Second": lambda x: [second_set.add(int(el)) for el in x],
    "Remove First": lambda x: [first_set.discard(int(el)) for el in x],
    "Remove Second": lambda x: [second_set.discard(int(el)) for el in x],
    "Check Subset": lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set))

}

for _ in range(int(input())):
    command_1, command_2, *data = input().split()
    command = command_1 + " " + command_2

    functions[command](data)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
