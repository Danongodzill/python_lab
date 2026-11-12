import math

radius = 5
cathetus1 = 6
cathetus2 = 8
items = 25
capacity = 6

circle_area = math.pi * radius ** 2
hypotenuse = math.sqrt(cathetus1 ** 2 + cathetus2 ** 2)
packages = math.ceil(items / capacity)

print("Площа круга:", round(circle_area, 2))
print("Гіпотенуза:", hypotenuse)
print("Потрібно упаковок:", packages)
