lst_in = ['8 11 -5', '3 4 10', '-1 -2 3', '4 5 6']
'''создает двумерный список с этими же значениями через запятую'''
lst2D = list(list(map(int, i.split())) for i in lst_in)


print(lst2D)
