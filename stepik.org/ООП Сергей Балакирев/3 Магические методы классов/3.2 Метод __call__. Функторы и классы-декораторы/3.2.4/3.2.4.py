"""
быстрое решение
class DigitRetrieve:
    def __call__(self, num):
        if num.isdigit() or num.startswith('-') and num[1:].isdigit():
            return int(num)

долгое решение
import re
class DigitRetrieve:
    def __call__(self, num):
        if re.fullmatch(r'-?\d+', num):
            return int(num)
"""


class DigitRetrieve:
    def __call__(self, num):
        try:
            return int(num)
        except Exception:
            return


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
