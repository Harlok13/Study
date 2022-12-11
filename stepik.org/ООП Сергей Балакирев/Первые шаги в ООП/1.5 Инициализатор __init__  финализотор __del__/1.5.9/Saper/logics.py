from main1 import *

def start_game():
    """Старт игры"""
    res = input('Желаете начать игру? y/n: ')
    return res in ['y', 'Y']

def choice_cell():
    """Выбрать клетку для открытия"""
    pass

def choice_board():
    """Выбрать размер поля и кол-во мин"""
    pass

if __name__ == '__main__':
    if start_game():

        while True:
            board = GamePole(4)
            board.open_cell(1, 1)
            board.show()

            input()
