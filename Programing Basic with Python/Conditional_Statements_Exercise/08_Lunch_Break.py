# 1. Име на сериал – текст
# 2. Продължителност на епизод – цяло число в диапазона [10… 90]
# 3. Продължителност на почивката – цяло число в диапазона [10… 120]

from math import ceil

serial_name = input()
serial_duration = int(input())
rest_duration = float(input())

lunch_time = rest_duration * 0.125
smoke_time = rest_duration * 0.25
left_time = rest_duration - lunch_time - smoke_time

# · Ако времето е достатъчно да изгледате епизода:
#     "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
# · Ако времето не Ви е достатъчно:
#     "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."

time_to_watch = ceil(left_time - serial_duration)
needed_time = ceil(serial_duration - left_time)

if left_time >= serial_duration:
    print(f"You have enough time to watch {serial_name} and left with {time_to_watch} minutes free time.")
else:
   print(f"You don't have enough time to watch {serial_name}, you need {needed_time} more minutes.")