class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id = 1
    d = {'name': (str,), 'weight': (int, float), 'price': (int, float)}

    # def __new__(cls, *args, **kwargs):
    #     cls.id += 1
    #     return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.id = Product.id
        Product.id += 1
        self.name = name
        self.weight = weight
        self.price = price

    # @classmethod
    # def get_id(cls):
    #     return cls.id

    def __setattr__(self, key, value):
        if key in self.d and type(value) in self.d.get(key):
            if (key == 'price' or key == 'weight') and value <= 0:
                raise TypeError('Неверный тип присваиваемых данных')
        elif key not in self.d:
            raise TypeError('Неверный тип присваиваемых данных')

        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError('Атрибут id удалять запрещено.')
        else:
            return super().__delattr__(item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

