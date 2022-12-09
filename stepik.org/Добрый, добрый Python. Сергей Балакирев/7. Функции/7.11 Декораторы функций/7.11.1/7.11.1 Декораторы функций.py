"""
Вычисление площади прямоугольника и отображение
с помощью декоратора
Без проверки на ввод (числа)
"""

def func_show(func):
    """Декоратор отображения результата вычисления"""
    def wrapper(*args, **kwargs):
        return print(f'Площадь прямоугольника: {func(*args, **kwargs)}')

    return wrapper


@func_show
def get_sq(width, height):
    """Вычисление площади прямоугольника"""
    return width * height


get_sq(11, 8)
