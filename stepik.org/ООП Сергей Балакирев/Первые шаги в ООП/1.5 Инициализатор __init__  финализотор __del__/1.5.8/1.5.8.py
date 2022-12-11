"""
Интересная задача, решил без просмотра видео

Ошибки в реализации:
создается копия списка, что занимает больше памяти
"""
class ListObject:

    def __init__(self, data: str):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj

    def __str__(self):
        return self.data


lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']


obj_lst = [ListObject(i) for i in lst_in]
[obj_lst[k].link(v) for k, v in enumerate(obj_lst[1:])]
head_obj = obj_lst[0]

print(obj_lst[0].__dict__)





