def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(BinarySearch([1,3,5,6,7,9], 9))

"""
def sudoku(puzzle):
    su = Sudoku(puzzle)
    su.board_solve()
    return su.table


class Sudoku:
    def __init__(self, table):
        self.table = table
        self.possible_board_list = [[[]] * 9] * 9

    @property
    def is_solved(self):
        for row in self.table:
            if 0 in row:
                return False
        return True

    def set_possible_board_list(self, row, col):
        g_row = self.get_row(row)
        g_col = self.get_col(col)
        g_square = self.get_square(row, col)
        possible_set = set(range(1, 10))
        remove_set = set(g_row + g_col + g_square)
        new_possible = list(possible_set - remove_set)
        self.possible_board_list[row][col] = new_possible

    def get_row(self, row):
        return [row_el for row_el in self.table[row] if row_el != 0]

    def get_col(self, col):
        return [row[col] for row in self.table if row[col] != 0]

    def get_square(self, row, col):
        item_row, item_col, square = int(row / 3), int(col / 3), []
        range_of_row = range(item_row * 3, (item_row * 3) + 3)
        range_of_col = range(item_col * 3, (item_col * 3) + 3)
        for i_row in range_of_row:
            for i_col in range_of_col:
                el = self.table[i_row][i_col]
                if el != 0:
                    square.append(el)

            return square

    def board_solve(self):
        while not self.is_solved:
            for row in range(9):
                for col in range(9):
                    if self.table[row][col] == 0:
                        self.set_possible_board_list(row, col)
                        if len(self.possible_board_list[row][col]) == 1:
                            self.table[row][col] = self.possible_board_list[row][col].pop()

"""
