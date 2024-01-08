data = input()
my_stack = [word for word in data]
for symbol in range(len(my_stack)):
    print(my_stack.pop(), end="")
