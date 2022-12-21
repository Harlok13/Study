from re import fullmatch


class PhoneBook:
    lst = []

    @classmethod
    def add_phone(cls, phone):
        cls.lst.append(phone)

    @classmethod
    def remove_phone(cls):
        if cls.lst:
            cls.lst.pop()

    @classmethod
    def get_phone_list(cls):
        return cls.lst


class PhoneNumber:
    def __init__(self, number, fio):
        if self.check_number(number):
            self.number = number
        self.fio = fio

    def __repr__(self):
        return f'{self.fio}: {self.number}'

    @staticmethod
    def check_number(number):
        return bool(fullmatch(r'^\d{11}$', str(number)))


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
p.remove_phone()
p.remove_phone()
p.remove_phone()
phones = p.get_phone_list()
print(phones)
