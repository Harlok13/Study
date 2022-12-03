"""Лямбду можно вызывать поставив в скобки.

>>> (lambda: print('Хай!'))()
Хай!
>>> (lambda a, b: a + b)(1, 2)
3

В лямбде можно использовать несколько действий подряд:
"""
(lambda a, b: (print("действие 1"), print("действие 2")))\
    (int(input()), int(input()))

"""
В лямбде можно использовать моржовый оператор присваивания
"""
(lambda a, b: (a := a + b, print(a)))(int(input()), int(input()))

"""
Можно так же преобразовать функцию get_filter на анонимную
"""
lst = [5, 3, 0, -6, 8, 10, -1]

get_filter = lambda a, filter=None: a if filter is None else [x for x in a if filter(x)]
print(get_filter(lst, lambda x: x % 2 == 0))
