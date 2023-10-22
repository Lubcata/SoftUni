cards = input().split(", ")
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split(", ")
    this_command = current_command[0]
    card_name = current_command[1]
    if this_command == "Add":
        if card_name in cards:
            print("Card is already in the deck")
        else:
            cards.append(card_name)
            print("Card successfully added")
    if this_command == "Remove":
        if card_name in cards:
            cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    if this_command == "Remove At":
        card_index = int(current_command[1])
        if card_index > len(cards):
            print("Index out of range")
        else:
            cards.remove(cards[card_index])
            print("Card successfully removed")
    if this_command == "Insert":
        card_index = int(current_command[1])
        card_name = current_command[2]
        if card_index < 0 or card_index > len(cards):
            print("Index out of range")
        else:
            if card_name in cards:
                print("Card is already added")
            else:
                cards.insert(card_index, card_name)
                print("Card successfully added")

print(", ".join(cards))
