"""
Декоратор преобразует список в "человеческий" список
"""
def show_menu(func):
    def wrapper(*args, **kwargs):
        [print(f'{k}. {v}') for k, v in enumerate(func(*args, **kwargs), 1)]

    return wrapper

@show_menu
def get_menu(s):
    return s.split()


get_menu('Главная Добавить Удалить Выйти')
