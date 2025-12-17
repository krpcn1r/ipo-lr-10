import collision

rect_correct = [(1, 1), (5, 5)]
rect_incorrect = [(5, 5), (1, 1)]

print(f"   Прямоугольник {rect_correct} корректный: {isCorrectRec(rect_correct)}")
print(f"   Прямоугольник {rect_incorrect} корректный: {isCorrectRec(rect_incorrect)}")

rect1 = [(1, 1), (4, 4)]
rect2 = [(2, 2), (5, 5)]
rect3 = [(6, 6), (8, 8)]

print(f"   Прямоугольник {rect1} и {rect2} пересекаются: {isCollisionRect(rect1, rect2)}")
print(f"   Прямоугольник {rect1} и {rect3} пересекаются: {isCollisionRect(rect1, rect3)}")

rect_a = [(0, 0), (3, 3)]
rect_b = [(1, 1), (4, 4)]
rect_c = [(5, 5), (7, 7)]

area_ab = intersectionAreaRect(rect_a, rect_b)
area_ac = intersectionAreaRect(rect_a, rect_c)

print(f"   Площадь пересечения {rect_a} и {rect_b}: {area_ab}")
print(f"   Площадь пересечения {rect_a} и {rect_c}: {area_ac}")

try:
    intersectionAreaRect([(1, 1), (5, 5)], [(6, 6), (3, 3)])
except RectCorrectError as e:
    print(f"   Поймано исключение: {e}")

rectangles1 = [
    [(1, 1), (5, 5)],
    [(2, 2), (6, 6)],
    [(3, 3), (7, 7)]
]

rectangles2 = [
    [(1, 1), (2, 2)],
    [(3, 3), (4, 4)],
    [(5, 5), (6, 6)]
]

rectangles3 = [
    [(0, 0), (10, 10)],
    [(2, 2), (8, 8)],
    [(3, 3), (7, 7)]
]

area1 = intersectionAreaMultiRect(rectangles1)
area2 = intersectionAreaMultiRect(rectangles2)
area3 = intersectionAreaMultiRect(rectangles3)

print(f"   Площадь пересечения всех прямоугольников в rectangles1: {area1}")
print(f"   Площадь пересечения всех прямоугольников в rectangles2: {area2}")
print(f"   Площадь пересечения всех прямоугольников в rectangles3: {area3}")

empty_list = []
print(f"   Площадь пересечения пустого списка: {intersectionAreaMultiRect(empty_list)}")

single_rect = [[(0, 0), (5, 5)]]
print(f"   Площадь пересечения одного прямоугольника: {intersectionAreaMultiRect(single_rect)}")

complex_rectangles = [
    [(0, 0), (8, 6)],     
    [(2, 1), (7, 5)],      
    [(3, 2), (6, 4)],      
    [(4, 2.5), (5.5, 3.5)] 
]

for i, rect in enumerate(complex_rectangles, 1):
    print(f"   {i}: {rect}")

for i in range(len(complex_rectangles)):
    for j in range(i + 1, len(complex_rectangles)):
        collides = isCollisionRect(complex_rectangles[i], complex_rectangles[j])
        print(f"   Прямоугольник {i+1} и {j+1}: {'пересекаются' if collides else 'не пересекаются'}")

complex_area = intersectionAreaMultiRect(complex_rectangles)
print(f"\n   Общая площадь пересечения всех прямоугольников: {complex_area}")

try:
    invalid_rectangles = [
        [(1, 1), (5, 5)],
        [(6, 6), (3, 3)], 
        [(2, 2), (7, 7)]
    ]
    result = intersectionAreaMultiRect(invalid_rectangles)
    print(f"   Результат: {result}")
except RectCorrectError as e:
    print(f"   Поймано исключение: {e}")

print("\n" + "=" * 50)

print("=" * 50)
