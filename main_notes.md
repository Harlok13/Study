*a, = 1, 2, 3, ... n

reversed()

___
```
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {i: text.count(i) for i in text}
print(result)
# {'f': 4, 'o': 9, 't': 9, 'b': 3, 'a': 8, 'l': 6, 'c': 6, 'y': 2, 'e': 10, 'r': 8, 'p': 4, 'u': 2, 'n': 6, 'k': 2, 'x': 1, 'i': 7, 'v': 1, 's': 4, 'h': 2, 'm': 3, 'd': 2}
```
___
https://stepik.org/lesson/446696/step/13?thread=solutions&unit=437002 (словари) решения

bisect()
insort()
solve()
format()
ljust()
divmod()

import itertools
float('-inf')


___
```
def sum_strings(x, y):
    l, res, carry = max(len(x), len(y)), "", 0
    x, y = x.zfill(l), y.zfill(l)
    for i in range(l-1, -1, -1):
        carry, d = divmod(int(x[i]) + int(y[i]) + carry, 10)
        res += str(d)
    return ("1" * carry + res[::-1]).lstrip("0") or "0"
```
