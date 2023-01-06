class Circle:
    def __init__(self, x, y, rad):
        self.__x = x
        self.__y = y
        self.__radius = rad

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            return super().__setattr__(key, value)
        raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):
        return False


circle = Circle(10.5, 7, 22)
circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует

print(circle.__dict__)
