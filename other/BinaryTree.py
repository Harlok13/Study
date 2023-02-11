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

        return self.preorder_search(current, find_val)

        # if self.preorder_search(current, find_val):
        #     return True
        # else:
        #     return False

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""

        if start:
            return find_val in self.tree_by_levels(start)
            # if find_val == start.value:
            #     return True
            # self.preorder_search(start.left, find_val)
            # self.preorder_search(start.right, find_val)

        # Set up tree

    def tree_by_levels(self, node):
        lst_of_nodes, depth = [], 0
        if node:
            lst_of_nodes.append([depth, node.value])
            if node.left:
                self.tree_by_levels_depth(depth, node.left, lst_of_nodes)
            if node.right:
                self.tree_by_levels_depth(depth, node.right, lst_of_nodes)
        lst_of_nodes = sorted(lst_of_nodes, key=lambda i: i[0])
        return [x[1] for x in lst_of_nodes]

    def tree_by_levels_depth(self, depth, node, lst_of_nodes):

        depth += 1
        lst_of_nodes.append([depth, node.value])
        if node:
            if node.left:
                self.tree_by_levels_depth(depth, node.left, lst_of_nodes)
            if node.right:
                self.tree_by_levels_depth(depth, node.right, lst_of_nodes)
        return lst_of_nodes


if __name__ == '__main__':
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

    assert tree.search(1) == True
    assert tree.search(3) == True
    assert tree.search(8) == False
    assert tree.search(0) == False
