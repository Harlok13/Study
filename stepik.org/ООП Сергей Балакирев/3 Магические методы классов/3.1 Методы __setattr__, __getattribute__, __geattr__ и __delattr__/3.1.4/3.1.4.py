class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        des = self.exhibits[indx]
        return f'Описание экспоната {des.name}: {des.descr}'


class Exhibits:
    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

    def get_info_exhibit(self):
        return f'Описание экспоната {self.name}: {self.descr}'


class Picture(Exhibits):
    def __init__(self, author, name, descr):
        super().__init__(name, descr)
        self.author = author


class Mummies(Exhibits):
    def __init__(self, location, name, descr):
        super().__init__(name, descr)
        self.location = location


class Papyri(Exhibits):
    def __init__(self, date, name, descr):
        super().__init__(name, descr)
        self.date = date


mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)
print(mus.exhibits[0].__dict__)
