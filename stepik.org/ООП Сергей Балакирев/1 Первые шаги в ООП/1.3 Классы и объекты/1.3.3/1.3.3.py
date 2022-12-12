# создаем в пустом классе новые атрибуты с помощью setattr
# выводим на экран значение атрибута color
class Car:
    pass


setattr(Car, 'model', 'Тойота')
setattr(Car, 'color', 'Розовый')
setattr(Car, 'number', 'П111УУ77')

print(Car.color)
