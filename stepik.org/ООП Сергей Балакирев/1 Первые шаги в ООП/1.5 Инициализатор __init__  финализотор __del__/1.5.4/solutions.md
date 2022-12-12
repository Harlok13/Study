### Александр Павлов

```
class TriangleChecker:
    def __init__(self, *args):
        self.abc = args

    def is_triangle(self):
        if any(type(x) not in (int, float) or x <= 0 for x in self.abc):
            return 1
        abc = sorted(self.abc)
        if sum(abc[:2]) <= abc[-1]:
            return 2
        return 3

a, b, c = map(int, input().split()) # эту строчку не менять
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
```

