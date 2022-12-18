class PathLines:
    def __init__(self, *args):
        self.start_x = self.start_y = 0
        self.lst = [*args]


class LineTo:
    lst = []

    def __new__(cls, *args, **kwargs):
        cls.lst += [super().__new__(cls)]
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    @classmethod
    def get_path(cls):
        return cls.lst

    @staticmethod
    def get_length():
        pass

    def add_line(self, line):
        pass


line1 = LineTo(10, 20)
line2 = LineTo(15, 25)
line3 = LineTo(20, 30)
p = PathLines(line1, line2, line3)
print(p.lst)
print(line1.get_path())
