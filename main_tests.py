class MyClass:
    def __init__(self, var):
        self.var = var

    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, value):
        if self.__validate(value):
            self.__var = value


    @staticmethod
    def __validate(value):
        return type(value) == int



c = MyClass('10')
print(c.__dict__)
