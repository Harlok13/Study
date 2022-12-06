import sys
"""

self.__dict__.update(zip(fields, lst_values))
"""
# здесь объявляется класс StreamData
class StreamData:

    def create(self, fields, lst_value):
        if len(lst_value) == 3:
            z = zip(fields, lst_value)
            for k, v in z:
                setattr(self, k, v)
            return True
        else:
            return False

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()


"""
fields = ('id', 'title', 'pages')
lst_value = [10, 'Название', 512]
if len(lst_value) == 3:
    z = zip(fields, lst_value)

for k, v in z:
    print(k, v)
"""
