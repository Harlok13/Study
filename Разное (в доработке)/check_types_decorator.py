class cList:
    def __init__(self, cType):
        self.cType = cType

    def check(self, values):
        if type(values) != list: raise TypeError
        for value in values:
            check(value, self.cType)


def check(value, cType):
    if cType == any:
        return
    elif type(cType) == cList:
        cType.check(value)
    elif type(value) != cType:
        raise TypeError


def strong(**kTypes):
    def checker(method):
        def wrapper(*args, **kwargs):
            for i, value in enumerate(args[1:]):
                cType = kTypes[list(kTypes.keys())[i]]
                check(value, cType)
            for key, value in kwargs.items():
                cType = kTypes[key]
                check(value, cType)
            method(*args, **kwargs)

        return wrapper

    return checker


class A:
    @strong(a=int, b=cList(int), c=any)
    def init(self, a, b, c):
        pass


A(1, [1, 2], "Hello")  # сработает

A(a=2.5, b="a", c=None)  # typeError
