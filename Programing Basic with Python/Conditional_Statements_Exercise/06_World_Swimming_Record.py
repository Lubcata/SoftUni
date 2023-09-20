# 1. Рекордът в секунди – реално число;
# 2. Разстоянието в метри – реално число;
# 3. Времето в секунди, за което плува разстояние от 1 м. - реално число.
from math import floor
record = float(input())
distance = float(input())
time_meter = float(input())

# · Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
#     o " Yes, he succeeded! The new world record is {времето на Иван} seconds."
# · Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
#     o "No, he failed! He was {недостигащите секунди} seconds slower."

time_all_distance = distance * time_meter
resistance = floor(distance / 15) * 12.5
final_time = time_all_distance + resistance
needed_seconds = final_time - record

if final_time < record:
    print(f"Yes, he succeeded! The new world record is {final_time :.2f} seconds.")
else:
    print(f"No, he failed! He was {needed_seconds :.2f} seconds slower.")