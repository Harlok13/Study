"""
Решено самостоятельно
"""

lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']

class DataBase:
    """База данных"""
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    @classmethod
    def lst_data_update(cls, data):
        """Преобразует переданный список значений в словари"""
        lst = [i.split() for i in data]
        cls.lst_data += [dict(zip(cls.FIELDS, i)) for i in lst]

    def select(self, a, b):
        """Возвращает выбранный диапазон"""
        return self.lst_data[a:b + 1]

    def insert(self, data):
        """Добавляет в lst_data новый словарь"""
        return self.lst_data_update(data)



db = DataBase()
db.insert(lst_in)

print(DataBase.__dict__)
print(DataBase.lst_data)
print(db.select(0, 3))


"""
Доп материал, использованный при решении

lst_data = []
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
FIELDS = ('id', 'name', 'old', 'salary')


lst = [i.split() for i in lst_in] # [['1', 'Сергей', '35', '120000'], ['2', 'Федор', '23', '12000'], ['3', 'Иван', '13', '1200']]

for i in lst:
    z = dict(zip(FIELDS, i))
    lst_data.append(z)

print(lst_data)
"""
