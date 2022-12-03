### Дмитрий Ткачук

```
def convert_string(data_type):
    def inner(numbers_string):
        return eval(f'{data_type}(map(int, numbers_string.split()))')
    return inner

print(
    convert_string(input())(input())
    )
```

___

### Алекс Глозман

Сокращенный варинат с лямбда функцией:
```
def parse(tp='list'):
    return lambda s: (tuple, list)[tp == 'list'](map(int, s.split()))

pr = parse(input())
print(pr(input()))
```

Развернутый вариант:

```
def parse(tp='list'):
    def inner(s):
        return (tuple, list)[tp == 'list'](map(int, s.split()))
    return inner

pr = parse(input())
print(pr(input()))
```
`(tuple, list)[tp == 'list']` это обращение к элементу кортежа по
индексу. Кортеж состоит из двух типов, которые по совместительству
являются ссылками на конструктор соотвествующего класса. Индексом в
кортеже будет значение логического выражения `tp == 'list'` приведенного
к целому значению. Выбранный конструктор будет применен к объекту
map. Например, если выполняется `tp == 'list'`  , то значение True 
будет приведено к числу `1`. Из кортежа выберется элемент по
индексу `1` - это будет конструктор списка `list`. В итоге выполнится
`list(map(int, s.split()))`.
