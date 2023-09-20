# •	Всички до 16 (вкл.) години се считат за деца и ще получат играчка
# •	Всички над 16 години се считат за възрастни и ще получат коледен пуловер
# •	Цената на всяка играчка е 5 лв., а цената на един пуловер е 15 лв.

# От конзолата се четат поредица от редове до получаване на команда "Christmas":
# •	Годините на всеки член от семейството - цяло число в интервала [1 … 130]

kids = 0
adults = 0
command = input()
toys = 0
dress = 0

while command != "Christmas":
    current_command = int(command)
    if current_command <= 16:
        kids += 1
        toys += 5
    elif current_command > 16:
        adults += 1
        dress += 15
    command = input()

# •	"Number of adults: {брой хора над 16 години}"
# •	"Number of kids: {брой хора до 16 (вкл.) години}"
# •	"Money for toys: {сумата за всички играчки}"
# •	"Money for sweaters: {сума за всички пуловери}"
print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys}")
print(f"Money for sweaters: {dress}")
