"""
Решено самостоятельно

Создаем список из 1000 экземпляров класса
Меняем цвет 2го экземпляра на желтый
"""

class Point:

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return self.color


points = [Point(i, i) for i in range(1, 2000, 2)]
points[1].color = 'yellow'






print(len(points), points[1], sep='\n')

print(points[1].__dict__)


p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

print(p1.__dict__, p2.__dict__, sep='\n')
