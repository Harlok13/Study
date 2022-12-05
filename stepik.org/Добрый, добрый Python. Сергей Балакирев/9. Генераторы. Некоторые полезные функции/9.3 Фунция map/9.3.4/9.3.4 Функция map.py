s_lst = ['house=дом', 'car=машина', 'men=человек', 'tree=дерево']
tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))


print(tp)
