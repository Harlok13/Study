# import operator
# import sys
# from pprint import pprint
#
# sys.path.append('/Users/macbook/PycharmProjects/Study/other')
# pprint(sys.path)
# import CustomCycle
# print(a := CustomCycle.CustomCycle([1, 2, 3]))
#
# # print(sub_examples.split_string('sdf,sdf;'))
# # sub_examples.sub_string()
# pprint(locals())
# print(operator.__eq__(4, 6))
#
# login, password = [input() for _ in '..']
# print(len(login) > 4 and len(password) > 8 and login != password)

# def get_adverts(
#         self, status=None, type=None, limit=None,
#         offset=None, order="id", direction="abs"
# ):
#     """
#     Список РК
#     Args:
#         order:
#         direction:
#     """
#     path = "/adv/v0/adverts?"
#
#     args = locals()
#     del args['self']
#     path = '/adv/v0/adverts?'
#     for arg, val in args.items():
#         if arg != 'self' and val is not None:
#             path = path + f'{arg}={val}&'
#     path = path[:-1]
#     return self._request(path, "GET")
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


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        self.nods = []

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        current = self.root

        if self.preorder_search(current, find_val):
            return True
        else:
            return False

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""

        if start is not None:
            if start.value == find_val:
                return True


            self.preorder_search(start.left, find_val)
            if find_val == start.value:
                return True
            else:
                return False
            self.preorder_search(start.right, find_val)

        # Set up tree


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))


         1
      2      3
   4     5
