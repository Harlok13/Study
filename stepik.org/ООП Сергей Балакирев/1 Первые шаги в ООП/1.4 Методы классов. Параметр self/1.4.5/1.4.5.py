"""
Решено самостоятельно

p.s. всего одна строчка заставила помучиться, эх
получилась какая-то костыльная проверка на дублирование

"""

class Translator:
    """Переводчик слов"""

    def __init__(self):
        self.d = {}

    @staticmethod
    def in_dictionary(key, dictionary):
        """Проверка наличия ключа в словаре"""
        return key in dictionary

    def add(self, eng, rus):
        """Добавление новых связок слов"""
        if self.in_dictionary(eng, self.d):
            if not rus in self.d[eng]:
                self.d[eng].append(rus)
        else:
            self.d[eng] = []
            self.d[eng].append(rus)


    def remove(self, eng):
        """Удаление слова"""
        # if self.in_dictionary(eng, self.d):
        self.d.pop(eng, False)  # можно через del


    def translate(self, eng):
        """Перевод слова"""
        return self.d[eng]


pairs = (('tree', 'дерево'), ('car', 'машина'),
         ('car', 'автомобиль'), ('leaf', 'лист'),
         ('river', 'река'), ('go', 'идти'),
         ('go', 'ехать'), ('go', 'ходить'),
         ('milk', 'молоко'))

tr = Translator()
for k, v in pairs:
    tr.add(k, v)

tr.remove('car')
tr.translate('go')





#
tr.add('tree', 'дерево')
tr.add('tree', 'дерево')
tr.add('tree', 'дерево')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('go', 'идти')
print(tr.translate('go'))

print(tr.__dict__)



