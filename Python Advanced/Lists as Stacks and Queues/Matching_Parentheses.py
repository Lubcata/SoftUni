expression = input()

stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    elif expression[index] == ")":
        first_index = stack.pop()
        last_index = index + 1
        print(expression[first_index:last_index])
