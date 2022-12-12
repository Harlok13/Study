"""
Регулярками было проще
"""

from re import fullmatch


class CardCheck:
    NUMBER_PATTERN = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    NAME_PATTERN = r'^[A-Z0-9]+?\s[A-Z0-9]+$'

    @classmethod
    def check_card_number(cls, number: str) -> bool:
        return bool(fullmatch(cls.NUMBER_PATTERN, number))

    @classmethod
    def check_name(cls, name: str) -> bool:
        return bool(fullmatch(cls.NAME_PATTERN, name))


print(CardCheck.check_card_number("3234-5475-9012-0000"))
print(CardCheck.check_name('SERGEI BALAKIREV'))
