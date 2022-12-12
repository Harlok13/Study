"""
Решено самостоятельно

set_data принимает данные
draw отображает полученные данные в указанном диапазоне,
определенный атрибутом класса LIMIT_Y

"""
class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data


    def draw(self):
        draw = self.data
        result = [i for i in draw if self.LIMIT_Y[1] >= i >= self.LIMIT_Y[0]]
        print(*result)


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
