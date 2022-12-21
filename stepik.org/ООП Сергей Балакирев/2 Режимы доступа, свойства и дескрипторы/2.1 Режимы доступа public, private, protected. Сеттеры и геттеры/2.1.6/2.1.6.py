"""
Очень хочется сделать через дескрипторы
"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.last = None

    def add_obj(self, obj):
        if self.head is None:
            self.tail = obj
            self.head = obj
            self.last = obj
        else:
            self.last.set_next(obj)
            obj.set_prev(self.last)
            self.tail = obj
            self.last = obj

    def remove_obj(self):
        self.last.get_prev().set_next(None)
        self.last.set_prev(None)
        self.last = self.last.get_prev()
        self.tail = self.tail.get_prev()

    def get_data(self):
        h = self.head
        lst = []
        while h.get_next() is not None:

            lst.append(h.get_data())
            h = h.get_next()
        return lst

class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
       self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        pass


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()
print(res)
lst.remove_obj()
print(lst.last.get_prev())
print(lst.last.get_next())
print(lst.last.get_prev())

