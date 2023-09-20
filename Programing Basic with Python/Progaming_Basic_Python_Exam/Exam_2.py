# •Първи ред – броят процесори, които трябва да се изработят – цяло число в интервала [1...500 000]
# •Втори ред – броят служители – цяло число в интервала [1...1000]
# •Трети ред – работните дни – цяло число в интервала [1...1000]
from math import floor

hours_of_work = 8
processors_to_hour = 3
processors_price = 110.10

processors_to_make = int(input())
number_of_employees = int(input())
work_days = int(input())

total_hours_of_work = number_of_employees * work_days * hours_of_work
made_processors = floor(total_hours_of_work / processors_to_hour)

profit = (made_processors - processors_to_make) * processors_price
losses = (processors_to_make - made_processors) * processors_price
# •	Ако са повече или колкото плануваните:
# o	"Profit: -> {печалби} BGN"
# •	Ако са по-малко от плануваните:
# o	"Losses: -> {загуби} BGN

if made_processors >= processors_to_make:
    print(f"Profit: -> {profit:.2f} BGN")
else:
    print(f"Losses: -> {losses:.2f} BGN")
