def foo(*args):
    assert len(args) != 0, f'Список не должен быть пустым'
    return round(sum(args) / len(args), 2)


if __name__ == '__main__':
    print(foo(4, 5, 6))

