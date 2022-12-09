"""
Решено самостоятельно

"""

class Graph:

    def __init__(self, data):
        self.data = data.copy()
        self.is_show = True


    def set_data(self, data):
        """Передача нового списка данных"""
        self.data = data


    def show_table(self):
        """Отображение данных в виде строки"""
        if self.is_show:
            print(*self.data)
        else:
            print('Отображение данных закрыто')


    def show_graph(self):
        """Отображение данных в виде графика"""
        if self.is_show:
            print('Графическое отображение данных:', *self.data)
        else:
            print('Отображение данных закрыто')


    def show_bar(self):
        """Отображение данных в виде столбчатой диаграммы"""
        if self.is_show:
            print('Столбчатая диаграмма:', *self.data)
        else:
            print('Отображение данных закрыто')


    def set_show(self, fl_show):
        """Изменение локального свойства"""
        self.is_show = fl_show






data_graph = [8, 11, 10, -32, 0, 7, 18]
gr = Graph(data_graph)
gr1 = Graph(data_graph)
gr.show_bar()
gr.show_table()
gr.set_show(False)
gr.show_graph()
gr.set_data([3, 6, 18, -35, 1, 21, 4])
gr.show_graph()
gr1.show_bar()
gr2 = Graph(data_graph)
gr2.show_bar()

print(id(gr.data))
print(id(gr1.data))
print(id(gr2.data))
