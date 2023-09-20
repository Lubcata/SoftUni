username = input()
current_password = input()
new_password = input()

while new_password != current_password:
    new_password = input()

print(f"Welcome {username}!")
