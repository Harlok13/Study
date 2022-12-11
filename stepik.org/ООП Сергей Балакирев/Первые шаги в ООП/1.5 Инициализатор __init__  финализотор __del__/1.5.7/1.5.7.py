"""
Решено самостоятельно

Дублирование убирается классметодом
либо наследованием
"""

class Cart:
    def __init__(self):
        self.goods = []

    def add(self, *args):
        self.goods += args

    def remove(self, indx):
        del self.goods[indx]  # pop чтобы не было ошибки

    def get_list(self):
        return ','.join([f'{i.name}: {i.price}' for i in self.goods]).split(',')

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


gd1 = TV('Телик1', 30_000)
gd2 = TV('Телик', 25_000)
gd3 = Table('Стол', 7_000)
gd4 = Notebook('Ноут1', 73_000)
gd5 = Notebook('Ноут2', 125_000)
cart = Cart()
cart.add(gd1, gd5, gd4, gd3, gd2)
print(cart.goods)
print(cart.get_list())
