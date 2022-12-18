class TreeObj:
    def __init__(self, indx, value=None):
        self.index = indx
        self.value = value
        self.left = self.right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    root = None

    @classmethod
    def predict(cls, root: 'DecisionTree', x: list[int]):
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next is None:
                break
            obj = obj_next
        return obj.value

    @classmethod
    def add_obj(cls, obj: TreeObj, node: 'DecisionTree' = None, left=True):
        """

        :param obj: reference to the newly added object
        :param node: a reference to the tree object to which node obj is attached
        :param left: flag that defines the branch of the tree to which the object is attached
        :return:
        """
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj

        return obj

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.index] == 1:
            return obj.left
        return obj.right


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)
print(res)
