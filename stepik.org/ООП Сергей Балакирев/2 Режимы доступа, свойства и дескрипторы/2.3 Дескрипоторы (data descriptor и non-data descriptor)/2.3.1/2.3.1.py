class FloatValue:
    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        setattr(instance, self._name, value)

    def __set_name__(self, owner, name):
        self._name = '_' + name

class Cell:
    table = FloatValue()
    def __init__(self):
        self.table = ...
