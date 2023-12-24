
result = ""

while True:
    command = input().split()

    if command[0] == "End":
        break
    elif command[0] == "Add":
        result += command[1]
    elif command[0] == "Upgrade":
        char_to_upgrade = command[1]
        upgraded_string = ""
        for char in result:
            if char == char_to_upgrade:
                upgraded_string += chr(ord(char) + 1)
            else:
                upgraded_string += char
        result = upgraded_string
    elif command[0] == "Print":
        print(result)
    elif command[0] == "Index":
        char_to_find = command[1]
        indices = [str(index) for index, char in enumerate(result) if char == char_to_find]
        if indices:
            print(" ".join(indices))
        else:
            print("None")
    elif command[0] == "Remove":
        substring_to_remove = command[1]
        result = result.replace(substring_to_remove, "")
