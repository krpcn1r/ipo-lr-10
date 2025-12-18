# main.py
from collision.utils import isCorrectRect, isCollisionRect, intersectionAreaRect, intersectionAreaMultiRect, RectCorrectError


# Задание 2
print("Задание 2:", isCorrectRect([(-3.4, 1), (9.2, 10)]))

# Задание 3
try:
    print("Задание 3:", isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))
    print("Задание 3:", isCollisionRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))
except RectCorrectError as e:
    print("Задание 3 Ошибка:", e)

# Задание 4
try:
    area2 = intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)])
    print("Задание 4 площадь:", area2)
except ValueError as e:
    print("Задание 4 Ошибка:", e)

# Задание 5 
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
try:
    multi_result = intersectionAreaMultiRect(rectangles)
    print(f"Задание 5 площадь пересечения всех прямоугольников: {multi_result}")
except RectCorrectError as e:
    print(e)
