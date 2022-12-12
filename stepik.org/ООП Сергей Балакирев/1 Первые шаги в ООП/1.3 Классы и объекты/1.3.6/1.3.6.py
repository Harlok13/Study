"""
Объявляем класс TravelBlog с атрибутом total_blogs, который
будет увеличиваться с каждым новым созданным экземпляром класса

Создаем 2 новых экземпляра класса
"""
class TravelBlog:
    total_blogs = 0

    @classmethod
    def count_total_blogs(cls):
        cls.total_blogs += 1

    def __init__(self, name, days):
        self.name = name
        self.days = days
        self.count_total_blogs()

    def __str__(self):
        return self.name


tb1 = TravelBlog('Франция', 6)
tb2 = TravelBlog('Италия', 5)

print(TravelBlog.__dict__)

"""
В случае, если не объявлять __init__ и декоратор classmethod

tb1 = TravelBlog()
setattr(tb1, 'name', 'Франция')
setattr(tb1, 'days', 6)
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = 'Италия'
tb2.days = 5
TravelBlog.total_blogs += 1

print(TravelBlog.__dict__)
"""
