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
        self.__radius = value

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)):
            return super().__setattr__(key, value)

