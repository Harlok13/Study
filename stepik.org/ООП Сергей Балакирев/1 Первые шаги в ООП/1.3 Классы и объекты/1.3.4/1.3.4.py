# получаем значение атрибута author и выводим результат на экран
class Notes:
    uid = 1005435
    title = 'Шутка'
    author = 'И.С. Бах'
    pages = 2


print(getattr(Notes, 'author', False))
