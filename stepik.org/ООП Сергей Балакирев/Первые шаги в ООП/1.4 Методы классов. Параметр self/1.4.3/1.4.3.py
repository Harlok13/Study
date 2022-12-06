import sys

# здесь объявляется класс StreamData
class StreamData:

    def create(self, fields, lst_value):
        self.fields = fields
        self.lst_value = lst_value
class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
