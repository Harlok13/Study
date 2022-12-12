class Point:
    __instance = None

    def __new__(cls, *args, **kwargs):
        __instance = super().__new__(cls)
        return __instance

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def clone(self):
        return Point(self.x, self.y)


pt = Point(10, 50)
pt_clone = Point.clone(pt)


print(id(pt.__dict__))
print(id(pt_clone.__dict__))

print(id(pt))
print(id(pt_clone))
