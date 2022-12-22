class FloatValue:
    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if self.__check_value(value):
            setattr(instance, self._name, value)


    def __set_name__(self, owner, name):
        self._name = '_' + name

    @staticmethod
    def __check_value(value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        return True


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell(float(x + 1) * float(i + 1)) for x in range(M)] for i in range(N)]




table = TableSheet(5, 3)
print(table.__dict__)
