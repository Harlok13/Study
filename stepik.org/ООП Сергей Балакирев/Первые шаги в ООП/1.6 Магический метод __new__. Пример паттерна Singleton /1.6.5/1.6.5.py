"""
Решено самостоятельно

Преобразует строку чисел в список вещественных чисел
"""


class Factory:
    @staticmethod
    def build_sequence():
        """Creating an empty list"""
        return []

    @staticmethod
    def build_number(string: str) -> float:
        """Converting float from string"""
        try:
            return float(string)
        except ValueError:
            print('invalid string format')


class Loader:
    @staticmethod
    def parse_format(string: str, factory: Factory) -> list:
        """Creating list of float from string"""
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


ld = Loader()
s = "4, 5, -6.5"
res = ld.parse_format(s, Factory())

print(res)
