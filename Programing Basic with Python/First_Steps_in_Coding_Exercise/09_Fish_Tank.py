# 1. Дължина в см – цяло число в интервала [10 … 500]
# 2. Широчина в см – цяло число в интервала [10 … 300]
# 3. Височина в см – цяло число в интервала [10… 200]
# 4. Процент – реално число в интервала [0.000 … 100.000]

lengh = int(input())
width = int(input())
height = int(input())
percent = float(input())

capacity = lengh * width * height
capacity_liters = capacity * 0.001
occupiet_space = percent * 0.01
needed_liters = capacity_liters * (1 - occupiet_space)
print(needed_liters)