# •	На първия ред - месецът - текст с възможности: "march", "april", "may", "june", "july", "august"
# •	На втория ред - броят на прекараните часове - цяло число в диапазона [1...10]
# •	На третия ред - броят на хората в групата -  цяло число в диапазона [1...10]
# •	На четвъртия ред - времето от деня – текст с възможности: "day" или "night"

month = input()
hours_in_room = int(input())
numbers_of_people = int(input())
type_of_day = input()
room_price = 0

if month == "march":
    room_price = 10.50
    if type_of_day == "night":
        room_price = 8.40
elif month == "april":
    room_price = 10.50
    if type_of_day == "night":
        room_price = 8.40
elif month == "may":
    room_price = 10.50
    if type_of_day == "night":
        room_price = 8.40
elif month == "june":
    room_price = 12.60
    if type_of_day == "night":
        room_price = 10.20
elif month == "july":
    room_price = 12.60
    if type_of_day == "night":
        room_price = 10.20
elif month == "august":
    room_price = 12.60
    if type_of_day == "night":
        room_price = 10.20

discount = 1

if numbers_of_people >= 4:
    discount = room_price * 0.1
    room_price -= discount
if hours_in_room >= 5:
    discount = room_price * 0.50
    room_price -= discount

# •	На първия ред: "Price per person for one hour: {цена на човек за час}"
# •	На втория ред: "Total cost of the visit: {общата цена}"

price_for_person_hour = room_price
total_cost = numbers_of_people * hours_in_room * price_for_person_hour

print(f"Price per person for one hour: {price_for_person_hour:.2f}")
print(f"Total cost of the visit: {total_cost:.2f}")
