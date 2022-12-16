"""
Посредственные знания мешают выполнить данное тз,
нужно сделать акцент на структуры данных

Пораскинув мозгами наконец нашел решение.
Радует, что сам сделал, хотя подсказка ввести
ссылку на последний эк помогла.
Правда, решение оказалось громоздким
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
        """
        При первом добавлении, last ссылается на новый объект.
        Если top is None, то top также ссылается на новый объект.
        При следующем добавлении идет проверка, если у last есть
        ссылка на объект, то у этого объекта вызывается сеттер, который
        перезаписывает локальный приватный атрибут next, теперь он
        ссылается на новый добавленный объект.
        После этого last ссылается уже на новый добавленный
        объект

        """
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        """
        Чтобы удалить эк из односвязного списка, нужно
        у предыдущего эк удалить ссылку на удаляемый эк
        p.s. пометки для себя, если буду перечитывать код:
        переменная t создается, чтобы не перезаписывать
        локальное свойство. result создает новую ссылку
        на свойство эк, что позволяет одновременно
        перезаписать и вернуть значение
        """
        if self.last:
            last = self.last
            t = self.top
            if t != last:
                while t.next != last:
                    t = t.next
                else:
                    result = t.next
                    t.next = None
                    self.last = t
                    return result
            else:
                result = self.top
                self.top = None
                self.last = None
                return result

    def get_data(self):
        if self.top:
            top = self.top
            lst = [top.data]
            while top != self.last:
                lst.append(top.next.data)
                top = top.next
            return lst

        return []


# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
#
#
# res = st.get_data()  # ['obj1', 'obj2']
# print(res)
# st.push(StackObj("obj4"))
# st.push(StackObj("obj5"))
# st.pop()
# st.pop()
# st.pop()
# st.pop()
# st.pop()
# st.pop()
#
#
# print(st.get_data())



