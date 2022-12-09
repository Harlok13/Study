"""
Без проверки на ввод (числа)

"""

def func_show(func):
    """Декоратор отображения результата вычисления"""
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'Площадь прямоугольника: {res}')
        return res

    return wrapper


@func_show
def get_sq(width, height):
    """Вычисление площади прямоугольника"""
    return width * height


get_sq(11, 8)
