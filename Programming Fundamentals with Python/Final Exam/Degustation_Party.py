guests = {}
while True:
    guest_info = input().split("-")
    command = guest_info[0]
    if command == "Stop":
        break
    quest = guest_info[1]
    meal = guest_info[2]
    if command == "Like":
        if quest not in guests.keys():
            guests[quest] = {"meal": []}

        guests[quest]["meal"].append(meal)
        print(guests)
    elif command == "Dislike":
        for curr_guest in guests[quest]["meal"]:
            if guests[quest]["meal"] == meal:
                guests[quest]["meal"].pop(meal)
    print(guests)