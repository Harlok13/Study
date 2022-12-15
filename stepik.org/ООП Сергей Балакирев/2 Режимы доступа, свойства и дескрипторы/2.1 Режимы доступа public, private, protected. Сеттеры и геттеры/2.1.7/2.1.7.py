from re import fullmatch
from random import choice, randint as r
import string as s

"""
P.S. не думал, что решу с первого раза
Валидация email заставляет напрячься в правильности написания
"""


class EmailValidator:
    symbols = f'{s.ascii_lowercase}{s.ascii_uppercase}{s.digits}_.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        return ''.join(choice(cls.symbols) for i in range(r(1, 200))) + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            res = fullmatch(r'^[A-Za-z0-9_.]+?@[A-Za-z0-9_.]+?\.[A-Za-z0-9_.]+?$', email)
            if res:
                lst = email.split('@')
                if len(lst[0]) <= 100 and len(lst[1]) <= 50 and lst[0].count('..') == 0 and lst[1].count('..') == 0:
                    return True
        return False

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


print(EmailValidator.check_email('i.like.this.course@my.stepik.domen.org'))
print(EmailValidator.get_random_email())
