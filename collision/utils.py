class RectCorrectError(Exception):
    def __init__(self, num):
        message = f"{num}-й прямоугольник некоректный"
        super().__init__(message)

def isCorrectRec(mas):
    if(mas[0][0] < mas[1][0] and mas[0][1] < mas[1][1]):
        return True
    else:
        return False

def isCollisionRect(mas1, mas2):
    x1 = mas1[0][0]
    x2 = mas1[1][0]
    x3 = mas2[0][0]
    x4 = mas2[1][0]
    y1 = mas1[0][1]
    y2 = mas1[1][1]
    y3 = mas2[0][1]
    y4 = mas2[1][1]
    if(isCorrectRec(mas1) == False): 
        raise RectCorrectError(1)
    elif(isCorrectRec(mas2) == False):
        raise RectCorrectError(2)
    if(x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2):
        return True
    else:
        return False

def intersectionAreaRect(mas1, mas2):
    x1 = mas1[0][0]
    x2 = mas1[1][0]
    x3 = mas2[0][0]
    x4 = mas2[1][0]
    y1 = mas1[0][1]
    y2 = mas1[1][1]
    y3 = mas2[0][1]
    y4 = mas2[1][1]
    if(isCorrectRec(mas1) == False):
        raise ValueError("1-й прямоугольник некоректный")    
    elif(isCorrectRec(mas2) == False):
        raise ValueError("2-й прямоугольник некоректный")
    if(isCollisionRect(mas1, mas2) == True):
        width = min(x2, x4) - max(x1, x3)
        height = min(y2, y4) - max(y1, y3)
        if(width <= 0 or height <= 0):
            return 0
        return width * height
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))  
