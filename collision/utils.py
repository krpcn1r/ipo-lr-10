# Обработка ошибок
class RectCorrectError(Exception):
    def __init__(self, num):
        message = f"{num}-й прямоугольник некоректный"
        super().__init__(message)

# Задание 2
def isCorrectRect(mas):
    if mas[0][0] < mas[1][0] and mas[0][1] < mas[1][1]:
        return True
    else:
        return False

# Задание 3
def isCollisionRect(mas1, mas2):
    if not isCorrectRect(mas1):
        raise RectCorrectError(1)
    if not isCorrectRect(mas2):
        raise RectCorrectError(2)
    
    # Координаты прямоугольников
    x1, y1 = mas1[0]
    x2, y2 = mas1[1]
    x3, y3 = mas2[0]
    x4, y4 = mas2[1]
    
    # Условие пересечения
    if x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2:
        return True
    else:
        return False

# Задание 4
def intersectionAreaRect(mas1, mas2):
    if not isCorrectRect(mas1):
        raise ValueError("1-й прямоугольник некорректный")
    if not isCorrectRect(mas2):
        raise ValueError("2-й прямоугольник некорректный")
    
    if not isCollisionRect(mas1, mas2):
        return 0
    
    # Вычисляем стороны прямоугольника
    width = min(mas1[1][0], mas2[1][0]) - max(mas1[0][0], mas2[0][0])
    height = min(mas1[1][1], mas2[1][1]) - max(mas1[0][1], mas2[0][1])
    
    return width * height

# Задание 5
def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0
    
    # Проверка всех на корректность 
    for i, rect in enumerate(rectangles, 1):
        if not isCorrectRect(rect):
            raise RectCorrectError(i)
    
    # Поиск общей области для всех прямоугольников одновременно
    x_left_max = rectangles[0][0][0]
    y_bottom_max = rectangles[0][0][1]
    x_right_min = rectangles[0][1][0]
    y_top_min = rectangles[0][1][1]
    
    for i in range(1, len(rectangles)):
        rect = rectangles[i]
        x_left_max = max(x_left_max, rect[0][0])
        y_bottom_max = max(y_bottom_max, rect[0][1])
        x_right_min = min(x_right_min, rect[1][0])
        y_top_min = min(y_top_min, rect[1][1])
    
    # Если границы не пересекаются, вычисляем площадь
    if x_left_max < x_right_min and y_bottom_max < y_top_min:
        return (x_right_min - x_left_max) * (y_top_min - y_bottom_max)
    return 0
