"""
Решено самостоятельно

Преобразует строку чисел в список вещественных чисел
"""


class Factory:
    def build_sequence(self):
        self.lst = []
        return self.lst

    def build_number(self, string: str) -> float:
        return float(string)


class Loader:
    def parse_format(self, string: str, factory: Factory) -> list:
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


ld = Loader()
s = "4, 5, -6.5"
res = ld.parse_format(s, Factory())

print(res)
