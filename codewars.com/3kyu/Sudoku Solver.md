Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.
```
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)
# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
```

# Solution
```python
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

```
