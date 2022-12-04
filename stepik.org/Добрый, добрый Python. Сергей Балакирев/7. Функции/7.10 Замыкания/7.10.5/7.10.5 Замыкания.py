def foo(s):
    '''
    На вход поступает строка из чисел (в данном
    случае последовательность чисел через пробел)

    Возвращает список или кортеж в зависимости
    от параметра tp
    '''
    def inner(tp):
        if tp == 'list':
            return list(map(int, s.split()))
        else:
            return tuple(map(int, s.split()))
    return inner


print(foo('-5 6 8 11 0 111 -456 3')('list'))
