"""
Посредственные знания мешают выполнить данное тз,
нужно сделать акцент на структуры данных
"""


class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if self.__check_next(obj):
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        if type(data) == str:
            self.__data = data

    @staticmethod
    def __check_next(value):
        return isinstance(value, StackObj | None)


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj: StackObj):
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        pass

    def get_data(self):
        pass


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))

res = st.get_data()    # ['obj1', 'obj2']
print(res)
