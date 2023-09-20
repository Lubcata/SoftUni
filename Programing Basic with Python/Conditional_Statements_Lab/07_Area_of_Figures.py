# · Ако фигурата е квадрат (square):
#  на следващия ред се чете едно дробно число - дължина на страната му

# · Ако фигурата е правоъгълник (rectangle): 
# на следващите два реда четат две дробни числа - дължините на страните му

# · Ако фигурата е кръг (circle): 
# на следващия ред чете едно дробно число - радиусът на кръга

# · Ако фигурата е триъгълник (triangle): 
# на следващите два реда четат две дробни числа - дължината на страната му и дължината на височината към нея

from math import pi

type_of_figure = input()
area = 0 

if type_of_figure == "square":
    side = float(input())
    area = side * side
elif type_of_figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
elif type_of_figure == "circle":
    radius = float(input())
    area = pi * (radius ** 2)
elif type_of_figure == "triangle":
    length = float(input())
    height = float(input())
    area = length * height / 2

print(f"{area:.3f}")