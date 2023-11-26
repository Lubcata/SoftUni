def decode(message, commadns):
    for command in commadns:
        token = command.split("|")
        instuction = token[0]
        
        if instuction == "Move":
            num_of_letters = int(token[1])
            message = message[num_of_letters:] + message[:num_of_letters]
        
        elif instuction == "Insert":
            index = int(token[1])
            value = token[2]
            message = message[:index] + value + message[index:]
        
        elif instuction == "ChangeAll":
            substring = token[1]
            replacement = token[2]
            message = message.replace(substring, replacement)
    
    print(f"The decrypted message is: {message}")


encrypted_message = input()
command_storage = []

while True:
    command = input()
    command_storage.append(command)
    if command == "Decode":
        break
    
decode(encrypted_message, command_storage)