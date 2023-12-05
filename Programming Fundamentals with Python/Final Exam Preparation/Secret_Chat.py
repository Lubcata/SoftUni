def change_all(message, substring, replacement):
    message = message.replace(substring, replacement)
    print(message)
    return message


def insert_space(message, index):
    message = message[:index] + ' ' + message[index:]
    print(message)
    return message


def reverse(message, substring):
    if substring in message:
        start_index_substring = message.index(substring[0])
        end_index_substring = start_index_substring + len(substring)
        message_with_removed_string = message[:start_index_substring] + message[end_index_substring:]
        reversed_word = substring[::-1]
        message = message_with_removed_string + reversed_word
        print(message)
    else:
        print("error")
    return message


def main():
    message = input()
    while True:
        command = input().split(":|:")
        action = command[0]
        if action == "Reveal":
            break
        if action == "InsertSpace":
            index = int(command[1])
            message = insert_space(message, index)
        elif action == "Reverse":
            substring = command[1]
            message = reverse(message, substring)
        elif action == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            message = change_all(message, substring, replacement)
    print(f"You have a new text message: {message}")


main()
