import collision

# Тестирование функции проверки корректности прямоугольника
rect_correct = [(1, 1), (5, 5)]  # Корректный: левый нижний, правый верхний
rect_incorrect = [(5, 5), (1, 1)]  # Некорректный: точки в неправильном порядке

print(f"   Прямоугольник {rect_correct} корректный: {isCorrectRec(rect_correct)}")
print(f"   Прямоугольник {rect_incorrect} корректный: {isCorrectRec(rect_incorrect)}")

# Тестирование функции определения пересечения прямоугольников
rect1 = [(1, 1), (4, 4)]
rect2 = [(2, 2), (5, 5)]  # Должны пересекаться с rect1
rect3 = [(6, 6), (8, 8)]  # Не должны пересекаться с rect1

print(f"   Прямоугольник {rect1} и {rect2} пересекаются: {isCollisionRect(rect1, rect2)}")
print(f"   Прямоугольник {rect1} и {rect3} пересекаются: {isCollisionRect(rect1, rect3)}")

# Тестирование функции вычисления площади пересечения двух прямоугольников
rect_a = [(0, 0), (3, 3)]
rect_b = [(1, 1), (4, 4)]  # Пересекаются с rect_a
rect_c = [(5, 5), (7, 7)]  # Не пересекаются с rect_a

area_ab = intersectionAreaRect(rect_a, rect_b)  # Площадь пересечения a и b
area_ac = intersectionAreaRect(rect_a, rect_c)  # Площадь пересечения a и c (должна быть 0)

print(f"   Площадь пересечения {rect_a} и {rect_b}: {area_ab}")
print(f"   Площадь пересечения {rect_a} и {rect_c}: {area_ac}")

# Тестирование обработки исключений для некорректных прямоугольников
try:
    # Некорректный прямоугольник: точки в неправильном порядке
    intersectionAreaRect([(1, 1), (5, 5)], [(6, 6), (3, 3)])
except RectCorrectError as e:
    print(f"   Поймано исключение: {e}")  # Должно выбросить исключение

# Тестирование функции вычисления площади пересечения нескольких прямоугольников
# Случай 1: Прямоугольники с частичным перекрытием
rectangles1 = [
    [(1, 1), (5, 5)],
    [(2, 2), (6, 6)],
    [(3, 3), (7, 7)]
]

# Случай 2: Непересекающиеся прямоугольники
rectangles2 = [
    [(1, 1), (2, 2)],
    [(3, 3), (4, 4)],
    [(5, 5), (6, 6)]
]

# Случай 3: Прямоугольники с полным вложением
rectangles3 = [
    [(0, 0), (10, 10)],   # Самый большой
    [(2, 2), (8, 8)],     # Внутри первого
    [(3, 3), (7, 7)]      # Внутри второго
]

# Вычисление площадей пересечения для всех трех случаев
area1 = intersectionAreaMultiRect(rectangles1)
area2 = intersectionAreaMultiRect(rectangles2)  # Должно быть 0
area3 = intersectionAreaMultiRect(rectangles3)  # Площадь самого маленького

print(f"   Площадь пересечения всех прямоугольников в rectangles1: {area1}")
print(f"   Площадь пересечения всех прямоугольников в rectangles2: {area2}")
print(f"   Площадь пересечения всех прямоугольников в rectangles3: {area3}")

# Тестирование граничных случаев
empty_list = []
print(f"   Площадь пересечения пустого списка: {intersectionAreaMultiRect(empty_list)}")  # Должно быть 0

single_rect = [[(0, 0), (5, 5)]]
print(f"   Площадь пересечения одного прямоугольника: {intersectionAreaMultiRect(single_rect)}")  # Площадь самого прямоугольника

# Тестирование со сложным набором прямоугольников
complex_rectangles = [
    [(0, 0), (8, 6)],      # Большой прямоугольник
    [(2, 1), (7, 5)],      # Частично перекрывающийся
    [(3, 2), (6, 4)],      # Еще больше вложенный
    [(4, 2.5), (5.5, 3.5)] # Самый маленький внутри всех
]

# Вывод всех прямоугольников для наглядности
for i, rect in enumerate(complex_rectangles, 1):
    print(f"   {i}: {rect}")

# Проверка попарных пересечений
for i in range(len(complex_rectangles)):
    for j in range(i + 1, len(complex_rectangles)):
        collides = isCollisionRect(complex_rectangles[i], complex_rectangles[j])
        print(f"   Прямоугольник {i+1} и {j+1}: {'пересекаются' if collides else 'не пересекаются'}")

# Вычисление общей площади пересечения всех прямоугольников
complex_area = intersectionAreaMultiRect(complex_rectangles)
print(f"\n   Общая площадь пересечения всех прямоугольников: {complex_area}")

# Тестирование обработки исключений в функции для нескольких прямоугольников
try:
    invalid_rectangles = [
        [(1, 1), (5, 5)],    # Корректный
        [(6, 6), (3, 3)],    # Некорректный - должен вызвать исключение
        [(2, 2), (7, 7)]     # Этот уже не будет обработан из-за исключения
    ]
    result = intersectionAreaMultiRect(invalid_rectangles)
    print(f"   Результат: {result}")
except RectCorrectError as e:
    print(f"   Поймано исключение: {e}")  # Должно выбросить исключение
