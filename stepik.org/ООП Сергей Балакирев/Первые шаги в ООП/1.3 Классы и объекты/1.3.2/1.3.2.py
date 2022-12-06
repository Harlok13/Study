# объявляем класс и прописываем ему атрибуты
# добавляем новый атрибут с помощью setattr
# еще один атрибут добавляем через класс
class Goods:
    title = 'Мороженое'
    weight = 154
    tp = 'Еда'
    price = 1024


setattr(Goods, 'price', 2048)
Goods.inflation = 100
