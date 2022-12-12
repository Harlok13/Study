"""
Решено самостоятельно

Создается список из 217 рандомных экземпляров 3 классов
с рандомными координатами
К экземплярам класса Line применяется метод reset_coords,
который обнуляет координаты
"""

from random import choice, randint as r, seed

class Figure:
    """Родительский класс"""

    def __init__(self, a, b, c, d):
        """Координаты верхнего правого и нижнего левого углов"""
        self.a, self.b, self.c, self.d  = a, b, c, d
        self.sp = (a, b)
        self.ep = (c, d)

    def reset_coords(self, a=0, b=0, c=0, d=0):
        """Изменить (обнулить) координаты"""
        self.a, self.b, self.c, self.d = a, b, c, d
        self.sp = (a, b)
        self.ep = (c, d)


class Line(Figure):
    pass


class Rect(Figure):
    pass


class Ellipse(Figure):
    pass


cls_lst = (Line, Rect, Ellipse)
# seed(1) не нужен в этом решении, странно
elements = [choice(cls_lst)(r(1, 100), r(1, 100), r(1, 100), r(1, 100)) for i in range(217)]

elements_1 = [i.reset_coords() for i in elements if isinstance(i, Line)]








