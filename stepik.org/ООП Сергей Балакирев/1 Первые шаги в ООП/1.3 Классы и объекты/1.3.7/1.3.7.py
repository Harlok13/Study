"""
Создается экземпляр класса, удаляется атрибут color и
оставшиеся атрибуты выводятся на экран
"""
class Figure:
    type_fig = 'ellipse'
    color = 'red'

    def __init__(self, start_pt, end_pt, color):
        self.start_pt = start_pt
        self.end_pt = end_pt
        self.color = color


fig1 = Figure((10, 5), (100, 20), 'blue')
delattr(fig1, 'color')

print(*fig1.__dict__)  # выводим только атрибуты экземпляра
