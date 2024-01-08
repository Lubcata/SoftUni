stack = []
n = int(input())

for _ in range(n):
    command = input().split()

    action = command[0]
    if action == '1':
        num_to_add = int(command[1])
        stack.append(num_to_add)
    elif action == '2':
        if stack:
            stack.pop()
    elif action == '3':
        print(max(stack))
    elif action == '4':
        print(min(stack))

reversed_string_stack = []

while stack:
    reversed_string_stack.append(str(stack.pop()))
print(", ".join(reversed_string_stack))
