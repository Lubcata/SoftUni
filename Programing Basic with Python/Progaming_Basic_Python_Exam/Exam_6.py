location_count = int(input())
total_dig = 0
work_days = 0
average_produce = 0
for locations in range(location_count):
    average_produce = float(input())
    work_days = int(input())
    total_dig = 0
    for days in range(work_days):
        dig_gold = float(input())
        total_dig += dig_gold
    average_dig = total_dig / work_days
    if average_dig >= average_produce:
        print(f"Good job! Average gold per day: {average_dig:.2f}.")
    elif average_dig < average_produce:
        print(f"You need {average_produce - average_dig:.2f} gold.")
