class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x, y):
        self.__x = 0
        self.__y = 0
        if self.__validate_coords(x, y):
            self.__x = x
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__validate_coords(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__validate_coords(value):
            self.__y = value

    @classmethod
    def __validate_coords(cls, *args):
        return all([i in range(cls.MIN_COORD, cls.MAX_COORD+1)
                    and type(i) == int or type(i) == float
                    for i in args])












