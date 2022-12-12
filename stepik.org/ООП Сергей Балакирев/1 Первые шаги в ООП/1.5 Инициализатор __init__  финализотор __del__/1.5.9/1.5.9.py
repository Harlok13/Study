class Cell:
    """Игровая клетка"""
    def __init__(self, around_mines: int=0, mine: bool=False):
        self.around_mines = around_mines
        self.mine = mine  # Наличие мины в клетке
        self.fl_open = False  # Открыта или закрыта клетка
        self.show_cell = '#' if not self.fl_open else self.around_mines  # если в дальнейшем захотим сделать часть поля открытым
    def __repr__(self):
        return f'{self.show_cell}'

class GamePole:
    """Игровое поле"""
    def __init__(self, N: int, M: int=0):
        self.N = N
        self.M = M
        self.pole = [[Cell() for i in range(self.N)] for j in range(self.N)]

    def init(self):
        # for i in range(self.M):  # M = 12
        #     self.pole.append()
        pass

    def show(self):
        [print(i) for i in self.pole]

    def open_cell(self, a=int(input()), b=int(input())):
        """а - номер линии, b - номер столбца"""
        self.pole[a-1][b-1].fl_open = True
        self.pole[a-1][b-1].show_cell = self.pole[a-1][b-1].around_mines


board = GamePole(4)
# print(board.pole)
board.open_cell()
board.show()

print(board.pole[0][0].__dict__)
