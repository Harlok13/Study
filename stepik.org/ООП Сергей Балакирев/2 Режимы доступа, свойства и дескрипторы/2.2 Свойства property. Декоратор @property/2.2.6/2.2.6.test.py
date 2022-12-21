from math import sqrt


class PathLines:
    def __init__(self, *args):
        self.start_x = self.start_y = 0
        self.lst = [*args]


    def get_path(self):
        return self.lst


    def get_length(self):
        l = len(self.lst) + 1
        lst = self.lst
        L = 0
        for i in range(l):
            if i != l:
                L += sqrt((pow(lst[i][0] - lst[i+1][0], 2) + pow(lst[i][1] - lst[i+1][1], 2)))
        return L

    @classmethod
    def add_line(self, line):
        self.lst.append(line)

class LineTo:

    # def __new__(cls, *args, **kwargs):
    #     cls.lst += [super().__new__(cls)]
    #     return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y






line1 = LineTo(10, 20)
line2 = LineTo(15, 25)
line3 = LineTo(20, 30)
p = PathLines(line1, line2, line3)
print(p.get_length())
print(p.get_path())
