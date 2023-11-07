def register(username, license_plate_number, users):
    if username in users:
        return f"ERROR: already registered with plate number {license_plate_number}"
    else:
        users[username] = license_plate_number
        return f"{username} registered {license_plate_number} successfully"

def unregister(username, users):
    if username not in users:
        return f"ERROR: user {username} not found"
    else:
        del users[username]
        return f"{username} unregistered successfully"
    
    
    
    
    
parking_users = {}
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split()
    current_task = current_command[0]
    current_username = current_command[1]
    if current_task == "register":
        current_license_plate = current_command[2]
        print(register(current_username, current_license_plate, parking_users))
    elif current_task == "unregister":
        print(unregister(current_username, parking_users))
        
for user in parking_users:
    print(f"{user} => {parking_users[user]}")
    