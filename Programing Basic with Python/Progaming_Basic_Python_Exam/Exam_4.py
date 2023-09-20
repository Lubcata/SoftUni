price_of_food = 12.45
small_cats = 0
big_cats = 0
huge_cats = 0
gram_food = 0
total_food = 0

cat_number = int(input())
for cats in range(cat_number):
    current_food = float(input())
    if current_food < 200:
        small_cats += 1
    elif current_food < 300:
        big_cats += 1
    elif current_food >= 300:
        huge_cats += 1
    total_food += current_food
total_food_price = total_food / 1000 * price_of_food
# "Group 1: {броят на котките в група 1: малки котки} cats."
# "Group 2: {броят на котките в група 2: големи котки} cats."
# "Group 3: {броят на котките в група 3: огромни котки} cats."
# "Price for food per day: {цената за храната} lv."
print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {total_food_price:.2f} lv.")
