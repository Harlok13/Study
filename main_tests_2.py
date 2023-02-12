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
