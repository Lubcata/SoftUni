time = int(input())
day = input()

# working time 10:00 - 18:00 in weekdays

if 10 <= time <= 18 and day == "Monday":
    print("open")

elif 10 <= time <= 18 and day == "Tuesday":
    print("open")

elif 10 <= time <= 18 and day == "Wednesday":
    print("open")
    
elif 10 <= time <= 18 and day == "Thursday":
    print("open")

elif 10 <= time <= 18 and day == "Friday":
    print("open")
elif 10 <= time <= 18 and day == "Saturday":
    print("open")
else:
    print("closed")