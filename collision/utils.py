class RectCorrectError(Exception):
    def __init__(self, num):
        message = f"{num}-й прямоугольник некоректный"
        super().__init__(message)

# Функция проверки корректности прямоугольника
def isCorrectRec(mas):
    if(mas[0][0] < mas[1][0] and mas[0][1] < mas[1][1]):
        return True
    else:
        return False

# Функция проверки пересечения двух прямоугольников
def isCollisionRect(mas1, mas2):
    # Извлекаем координаты прямоугольников для удобства
    x1 = mas1[0][0]
    x2 = mas1[1][0]
    x3 = mas2[0][0]
    x4 = mas2[1][0]
    y1 = mas1[0][1]
    y2 = mas1[1][1]
    y3 = mas2[0][1]
    y4 = mas2[1][1]
    
    # Проверяем корректность прямоугольников
    if(isCorrectRec(mas1) == False): 
        raise RectCorrectError(1)  # Первый прямоугольник некорректен
    elif(isCorrectRec(mas2) == False):
        raise RectCorrectError(2)  # Второй прямоугольник некорректен
    
    # Условие пересечения: проекции пересекаются по обеим осям
    if(x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2):
        return True
    else:
        return False

# Функция вычисления площади пересечения двух прямоугольников
def intersectionAreaRect(mas1, mas2):
    # Извлекаем координаты
    x1 = mas1[0][0]
    x2 = mas1[1][0]
    x3 = mas2[0][0]
    x4 = mas2[1][0]
    y1 = mas1[0][1]
    y2 = mas1[1][1]
    y3 = mas2[0][1]
    y4 = mas2[1][1]
    
    # Проверяем корректность
    if(isCorrectRec(mas1) == False):
        raise RectCorrectError(1)    
    elif(isCorrectRec(mas2) == False):
        raise RectCorrectError(2)
    
    # Если есть пересечение, вычисляем площадь
    if(isCollisionRect(mas1, mas2) == True):
        width = min(x2, x4) - max(x1, x3)
        height = min(y2, y4) - max(y1, y3)
        # Проверка на случай отрицательных размеров (паранойя)
        if(width <= 0 or height <= 0):
            return 0
        return width * height
    return 0

# Функция вычисления площади пересечения нескольких прямоугольников
def intersectionAreaMultiRect(rectangles):
    # Обработка пустого списка
    if not rectangles:
        return 0
    
    # Проверка корректности всех прямоугольников
    for i, rect in enumerate(rectangles, 1):
        if not isCorrectRec(rect):
            raise RectCorrectError(i)  # i-й прямоугольник некорректен
    
    x_left_max = rectangles[0][0][0]    # Максимальная левая граница
    y_bottom_max = rectangles[0][0][1]  # Максимальная нижняя граница
    x_right_min = rectangles[0][1][0]   # Минимальная правая граница
    y_top_min = rectangles[0][1][1]     # Минимальная верхняя граница
    
    # Обновление границ для всех остальных прямоугольников
    for i in range(1, len(rectangles)):
        rect = rectangles[i]
        
        x_left_max = max(x_left_max, rect[0][0])
        y_bottom_max = max(y_bottom_max, rect[0][1])
        x_right_min = min(x_right_min, rect[1][0])
        y_top_min = min(y_top_min, rect[1][1])
    
    # Проверяю, существует ли общая область пересечения
    if x_left_max < x_right_min and y_bottom_max < y_top_min:
        width = x_right_min - x_left_max
        height = y_top_min - y_bottom_max
        return width * height
    else:
        return 0  # Нет общей области пересечения

if __name__ == "__main__":
    # Пример 1: Частично пересекающиеся прямоугольники
    rects1 = [
        [(1, 1), (5, 5)],   # Прямоугольник 1
        [(2, 2), (6, 6)],   # Прямоугольник 2 (пересекается с 1)
        [(3, 3), (7, 7)]    # Прямоугольник 3 (пересекается с 1 и 2)
    ]
    print(f"Пример 1: {intersectionAreaMultiRect(rects1)}")  
    
    # Пример 2: Непересекающиеся прямоугольники
    rects2 = [
        [(1, 1), (2, 2)],  
        [(3, 3), (4, 4)],   
        [(5, 5), (6, 6)]    
    ]
    print(f"Пример 2: {intersectionAreaMultiRect(rects2)}")  
    
    # Пример 3: Один прямоугольник
    rects3 = [
        [(0, 0), (10, 10)] 
    ]
    print(f"Пример 3: {intersectionAreaMultiRect(rects3)}") 
    
    # Пример 4: Некорректный прямоугольник (обработка исключения)
    try:
        rects4 = [
            [(1, 1), (5, 5)],   
            [(6, 6), (3, 3)],  
            [(2, 2), (7, 7)]   
        ]
        print(f"Пример 4: {intersectionAreaMultiRect(rects4)}")
    except RectCorrectError as e:
        print(f"Пример 4: Ошибка - {e}")  # Должно вывести: "2-й прямоугольник некоректный"
