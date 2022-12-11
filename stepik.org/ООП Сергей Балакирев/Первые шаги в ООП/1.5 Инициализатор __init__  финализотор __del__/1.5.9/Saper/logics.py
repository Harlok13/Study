from main1 import *


def validation(func):
    def wrapper(*args):
        try:
            lst = list(map(int, args))
        except TypeError:
            print('Нужно ввести целое число')
        except Exception:
            print('Что-то пошло не так')
        return func(*lst)

        # if all([True if type(i) == type else False for i in args]):
        #     return func(*args)
        # raise ValueError('Значение должно быть целым числом')

    return wrapper




def start_game():
    """Старт игры"""
    res = input('Желаете начать игру? y/n: ')
    return res in ['y', 'Y']

@validation
def choice_cell():
    """Выбрать клетку для открытия"""
    a = input('Напишите номер линии, которую открыть: ')
    b = input('Напишите номер столбца, который открыть: ')
    return (a, b)

def choice_board():
    """Выбрать размер поля и кол-во мин"""
    pass

if __name__ == '__main__':
    if start_game():

        while True:  # сделать валидацию выбора, пока пользователь не согласится, цикл будет повторяться
            board = GamePole(4)
            board.open_cell(*choice_cell())
            board.show()

            input()
