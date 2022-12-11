"""
Создаем только первые 5 объектов
"""


class SingletonFive:
    __instance = None
    __counter = 0

    def __new__(cls, *args, **kwargs):
        if cls.__counter < 5:
            cls.__counter += 1
            cls.__instance = super().__new__(cls)
            cls.__instance.name = args[0]

        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(i) for i in range(10)]
print(objs[0].name)
print(objs)
