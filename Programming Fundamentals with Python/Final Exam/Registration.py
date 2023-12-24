import re
success_registration = 0
number_users = int(input())
for current_user in range(number_users):
    data = input()
    pattern = r"([U\$]+)([A-Z][a-z]{2,})(\1)([P\@\$]+)([a-zA-Z]{5,}[\d]{1,})(\4)"
    match = re.search(pattern, data)
    if match:
        print("Registration was successful")
        success_registration += 1
        username = match.group(2)
        password = match.group(5)
        print(f"Username: {username}, Password: {password}")
    else:
        print("Invalid username or password")

print(f"Successful registrations: {success_registration}")

