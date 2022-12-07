lst_data = []
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
FIELDS = ('id', 'name', 'old', 'salary')


lst = [i.split() for i in lst_in] # [['1', 'Сергей', '35', '120000'], ['2', 'Федор', '23', '12000'], ['3', 'Иван', '13', '1200']]

for i in lst:
    z = dict(zip(FIELDS, i))
    lst_data.append(z)

print(lst_data)
