class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class DecisionTree:
    @classmethod
    def predict(cls, root: 'DecisionTree', x):
        pass

    @classmethod
    def add_obj(cls, obj: TreeObj, node: 'DecisionTree' = None, left=True):
        pass
