class RectCorrectError(Exception):
    def __init__(self, num):
        message = f"{num}-й прямоугольник некоректный"
        super().__init__(message)

def isCorrectRec(mas):
    if(mas[0][0] < mas[1][0] and mas[0][1] < mas[1][1]):
        return True
    else:
        return False

def isCollisionRect(mas):
    if(isCorrectRec(mas[0]) == False): 
        raise RectCorrectError(1)
    elif(isCorrectRec(mas[1]) == False):
        raise RectCorrectError(2)
    if(mas[0][0][0] < mas[1][1][0] and mas[1][0][0] < mas[0][1][0] and mas[0][0][1] < mas[1][1][1] and mas[1][0][1] < mas[0][1][1]):
        return True
    else:
        return False
