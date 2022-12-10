def sorted_lst(func):
    """Сортировка списка чисел"""
    def wrapper(*args, **kwargs):
        return sorted(func(*args, **kwargs))

    return wrapper

@sorted_lst
def get_list(s):
    """Преобразует строку в список целых чисел"""
    return list(map(int, s.split()))


print(*get_list(['8 11 -5 4 3 10']))


