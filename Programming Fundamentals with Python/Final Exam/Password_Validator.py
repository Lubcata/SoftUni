password = input()

while True:
    command = input().split()
    action = command[0]
    if action == 'Complete':
        break
    if action == 'Make':
        sec_action = command[1]
        index = int(command[2])
        if sec_action == 'Upper':
            password = password[:index] + password.upper()[index:index + 1] + password[index + 1:]
            print(password)
        elif sec_action == 'Lower':
            password = password[:index] + password.lower()[index:index + 1] + password[index + 1:]
            print(password)
    elif action == 'Insert':
        index = int(command[1])
        char = command[2]
        password = password[:index] + char + password[index:]
        print(password)
    elif action == 'Replace':
        char = command[1]
        value = int(command[2])
        if char in password:
            ascii_char = int(ord(char)) + value
            new_char = chr(ascii_char)

            print(new_char)
            for letter in password:
                if letter == char:
                    letter = new_char
                print(password)
    elif action == 'Validation':
        if password.len() < 8:
            print("Password must be at least 8 characters long!")
        elif chr(password) not in password and