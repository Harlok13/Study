"""Функция вызывает саму себя, вторым выражением подставляются значения"""
(lambda a: print(abs(a)))(float(input()))
