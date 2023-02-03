# def BinarySearch(lys, val):
#     first = 0
#     last = len(lys)-1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first+last)//2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val<lys[mid]:
#                 last = mid -1
#             else:
#                 first = mid +1
#     return index
#
# print(BinarySearch([1,3,5,6,7,9], 9))


game_stamps = [{'offset': 0, 'score': {'away': 0, 'home': 0}},
               {'offset': 2, 'score': {'away': 0, 'home': 0}},
               {'offset': 3, 'score': {'away': 0, 'home': 0}},
               {'offset': 6, 'score': {'away': 0, 'home': 0}},
               {'offset': 7, 'score': {'away': 0, 'home': 0}},
               {'offset': 10, 'score': {'away': 0, 'home': 0}},
               {'offset': 12, 'score': {'away': 0, 'home': 0}},
               {'offset': 15, 'score': {'away': 0, 'home': 0}},
               {'offset': 18, 'score': {'away': 0, 'home': 0}},
               {'offset': 21, 'score': {'away': 0, 'home': 0}},
               {'offset': 22, 'score': {'away': 0, 'home': 0}},
               {'offset': 23, 'score': {'away': 0, 'home': 0}},
               {'offset': 26, 'score': {'away': 0, 'home': 0}},
               {'offset': 28, 'score': {'away': 0, 'home': 0}},
               {'offset': 29, 'score': {'away': 0, 'home': 0}},
               {'offset': 30, 'score': {'away': 0, 'home': 0}},
               {'offset': 32, 'score': {'away': 0, 'home': 0}},
               {'offset': 35, 'score': {'away': 0, 'home': 0}},
               {'offset': 38, 'score': {'away': 0, 'home': 0}},
               {'offset': 41, 'score': {'away': 0, 'home': 0}},
               {'offset': 42, 'score': {'away': 0, 'home': 0}},
               {'offset': 43, 'score': {'away': 0, 'home': 0}},
               {'offset': 46, 'score': {'away': 0, 'home': 0}},
               {'offset': 48, 'score': {'away': 0, 'home': 0}},
               {'offset': 50, 'score': {'away': 0, 'home': 0}},
               {'offset': 53, 'score': {'away': 0, 'home': 0}},
               {'offset': 55, 'score': {'away': 0, 'home': 0}},
               {'offset': 57, 'score': {'away': 0, 'home': 0}},
               {'offset': 59, 'score': {'away': 0, 'home': 0}},
               {'offset': 60, 'score': {'away': 0, 'home': 0}},
               {'offset': 62, 'score': {'away': 0, 'home': 0}},
               {'offset': 63, 'score': {'away': 0, 'home': 0}},
               {'offset': 64, 'score': {'away': 0, 'home': 0}},
               {'offset': 66, 'score': {'away': 0, 'home': 0}},
               {'offset': 68, 'score': {'away': 0, 'home': 0}},
               {'offset': 70, 'score': {'away': 0, 'home': 0}},
               {'offset': 72, 'score': {'away': 0, 'home': 0}},
               {'offset': 75, 'score': {'away': 0, 'home': 0}},
               {'offset': 77, 'score': {'away': 0, 'home': 0}},
               {'offset': 79, 'score': {'away': 0, 'home': 0}},
               {'offset': 82, 'score': {'away': 0, 'home': 0}},
               {'offset': 83, 'score': {'away': 0, 'home': 0}},
               {'offset': 85, 'score': {'away': 0, 'home': 0}},
               {'offset': 88, 'score': {'away': 0, 'home': 0}},
               {'offset': 90, 'score': {'away': 0, 'home': 0}},
               {'offset': 92, 'score': {'away': 0, 'home': 0}},
               {'offset': 95, 'score': {'away': 0, 'home': 0}},
               {'offset': 98, 'score': {'away': 0, 'home': 0}},
               {'offset': 101, 'score': {'away': 0, 'home': 0}},
               {'offset': 104, 'score': {'away': 0, 'home': 0}},
               {'offset': 107, 'score': {'away': 0, 'home': 0}}]

def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    indx = get_offset(game_stamps, offset)

    return game_stamps[indx]['score']['home'], game_stamps[indx]['score']['away']


def get_offset(game_stamps, target):
    first = 0
    last = len(game_stamps) - 1
    indx = -1
    while (first <= last) and (indx == -1):
        mid = (first + last) // 2
        if game_stamps[mid]['offset'] == target:
            indx = mid
        else:
            if target < game_stamps[mid]['offset']:
                last = mid - 1
            else:
                first = mid + 1
    else:
        if first > last:
            return last
    return indx

print(get_offset(game_stamps, 31))
print(get_score(game_stamps, 31))

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
