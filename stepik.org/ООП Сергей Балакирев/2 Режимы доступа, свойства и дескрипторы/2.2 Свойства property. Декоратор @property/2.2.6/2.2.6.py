class PathLines:
    def __init__(self, *args):
        self.start_x = self.start_y = 0
        self.next = ...
        for i in args:
            start = None
            if start is None:
                start = i
            else:
                start.next = i
                start = i


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

    @staticmethod
    def get_path():
        pass

    @staticmethod
    def get_length():
        pass

    def add_line(self, line):
        pass

