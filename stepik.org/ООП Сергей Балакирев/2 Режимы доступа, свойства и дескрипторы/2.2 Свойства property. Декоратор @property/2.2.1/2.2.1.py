class Car:
    # def __init__(self, model):
    #     self.__model = None
    #     if self.__check_model(model):
    #         self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__check_model(model):
            self.__model = model

    @staticmethod
    def __check_model(model):
        return type(model) == str and len(model) in range(2, 101)


car = Car()
car.model = 'Toyota'
print(car.model)
