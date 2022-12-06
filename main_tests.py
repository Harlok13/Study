fields = ('id', 'title', 'pages')
lst_value = [10, 'Название', 512]
if len(lst_value) == 3:
    z = zip(fields, lst_value)

for k, v in z:
    print(k, v)
