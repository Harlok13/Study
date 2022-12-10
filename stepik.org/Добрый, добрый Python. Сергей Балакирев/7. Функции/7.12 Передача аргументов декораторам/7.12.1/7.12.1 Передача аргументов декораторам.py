"""
Функция get_sum выполняет сразу 2 задачи: преобразует
строку в список и вычисляет сумму, что не есть правильно.
Функция должна выполнять только одну задачу.
Но сделал по тз
"""
def get_start(start=5):
    def dec(func):
        return lambda *args, **kwargs: func(*args, **kwargs) + start

    return dec
@get_start()
def get_sum(s):
    return sum(map(int, s.split()))

print(get_sum('1 4 2 5'))
