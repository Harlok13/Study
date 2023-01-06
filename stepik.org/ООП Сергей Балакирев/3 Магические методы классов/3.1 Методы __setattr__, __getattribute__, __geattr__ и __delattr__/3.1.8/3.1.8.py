import time


class GeyserClassic:
    MAX_DATE_FILTER = 100
    slots = {1: [], 2: [], 3: []}

    @staticmethod
    def check_slots(slot_num, filter):
        if slot_num - 1 in range(3):
            return (isinstance(filter, Mechanical), isinstance(filter, Aragon), isinstance(filter, Calcium))[slot_num - 1]

    @classmethod
    def add_filter(cls, slot_num, filter):
        if cls.slots.get(slot_num, None) == [] and cls.check_slots(slot_num, filter):
            cls.slots.get(slot_num).append(filter)

    @classmethod
    def remove_filter(cls, slot_num):
        if cls.slots.get(slot_num, None):
            cls.slots.get(slot_num).clear()

    def get_filters(self):
        return tuple((i for i in self.slots.values()))

    def water_on(self):
        if all([bool(i) for i in self.slots.values()]):
            if len([i for i in self.slots.values() if i[0].date in range(0, self.MAX_DATE_FILTER + 1)]) == 3:
                return True
        return False


class Filter:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        super().__setattr__(key, value)



class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print(my_water.water_on())
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print(my_water.water_on())
print(my_water.slots)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
print(f1, f2, f3)
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
