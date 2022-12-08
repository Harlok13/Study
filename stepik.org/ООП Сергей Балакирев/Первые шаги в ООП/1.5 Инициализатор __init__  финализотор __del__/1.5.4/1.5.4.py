"""
Решено самостоятельно

Комментарий для себя:
ужасная реализация валидности
много повторяющегося кода
или нет? Впрочем, пока не могу понять

В любом случае лучший вариант
проверки на возможность построить треугольник это:
if max(coord) > (sum(coord)-max(coord))
изначально координаты поместить в список
и реализовать цикл
"""

class TriangleChecker:

    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c


    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        if not (type(a) in (int, float)) or not (type(b) in (int, float)) or not (type(c) in (int, float)):
            return 1
        elif a <= 0 or b <= 0 or c <= 0:
            return 1
        if a + b > c and b + c > a and a + c > b:
            return 3
        else:
            return 2


tr = TriangleChecker(3, 0, 5)
print(tr.is_triangle())

