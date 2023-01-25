from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args):
        return sum(func(*args))

    return wrapper


@decorator
def get_list(s):
    """Функция для формирования списка целых значений"""
    return list(map(int, s.split()))

if __name__ == '__main__':
    get_list("1 2 3 -1 -2 -3")
