from random import randint as r
a, b, c = 1, 2, 3
lst = [1, 2, 3]
ma = max(lst)
mi = min(lst)
print(set([f'{r(mi, ma)}{r(mi, ma)}{r(mi, ma)}' for i in range(333)]))


