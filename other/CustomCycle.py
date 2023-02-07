from collections import namedtuple
from typing import Any


class CustomCycle:
    """Самописный класс cycle из itertools"""

    def __init__(self, iterable: iter, *, start: int = 0):
        self.start = start
        self.end = len(iterable)
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self) -> Any:
        value = None
        if self.start >= self.end:
            self.start = 0
        value = self.iterable[self.start]
        self.start += 1
        return value


def test_custom_cycle(tests_case: iter):
    for expected, arg in tests_case.items():
        test_case = CustomCycle(arg[0], start=arg[1])
        result = [next(test_case) for _ in range(8)]
        assert result == list(expected), f'result: {result} - expected: {list(expected)}'
        print('passed')


# при 8 итерациях (нехешируемые ключи не проверяются в этом тесте)
examples = {
    (8, 9, 7, 66, 8, 9, 7, 66): ([8, 9, 7, 66], 0),
    ('c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'): (['a', 'b', 'c', 'd'], 2),
    (7.5, 6.0, 8.3, 7.5, 6.0, 8.3, 7.5, 6.0): ([8.3, 7.5, 6.0], 1),
    ('a', 4, 4.3, 'a', 4, 4.3, 'a', 4): (['a', 4, 4.3], 0),
    ((2,), (3, 4, 5), (3, 4), (2,), (3, 4, 5), (3, 4), (2,), (3, 4, 5)): ([(3, 4), (2,), (3, 4, 5)], 1),
    (True, False, 25, (True, False), True, False, 25, (True, False)): ([True, False, 25, (True, False)], 0)
}

if __name__ == '__main__':
    test = CustomCycle([8, 9, 7, 66], start=0)
    res = [next(test) for _ in range(8)]
    assert res == [8, 9, 7, 66, 8, 9, 7, 66], f'{res}'

    test = CustomCycle(['a', 'b', 'c', 'd'], start=2)
    res = [next(test) for _ in range(8)]
    assert res == ['c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'], f'{res}'

    test_custom_cycle(examples)
