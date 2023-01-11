from collections import Counter
from pprint import pprint


def foo(*, start, end):
    return start + end

c = Counter('sdfskl')


if __name__ == '__main__':
    print(list(c.elements()))
    print(foo(start=3, end=4))

