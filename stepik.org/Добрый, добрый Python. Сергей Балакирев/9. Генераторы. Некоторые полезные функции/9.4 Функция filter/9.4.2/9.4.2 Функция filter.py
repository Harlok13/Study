lst_in = ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']

lst = [tuple(i.split('=')) for i in lst_in]  # создаем список кортежей

result = filter(lambda x: x if int(x[1]) >= 500 else None, lst)  # фильтруем по весу
# можно обойтись просто int(x[1]) >= 500 (важно только булева значение)

print(*(i[0] for i in result))  # выбираем только названия
