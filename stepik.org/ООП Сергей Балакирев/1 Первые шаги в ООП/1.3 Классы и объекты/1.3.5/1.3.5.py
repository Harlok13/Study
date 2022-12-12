# выводим на экран значение атрибута rus_word, в случае его отсутствия выводим False
class Dictionary:
    rus = 'Питон'
    eng = 'Python'


print(getattr(Dictionary, 'rus_word', False))
