from string import ascii_lowercase as asc
"""
Создает генератор, в котором хранятся строки 
aa ab ac и т.д.
"""
gen = (i + j for i in asc for j in asc)
"Выводим на экран первые 50 строк"
print(*(next(gen) for i in range(50)))
