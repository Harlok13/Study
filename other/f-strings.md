![](../img/format_str.jpg)

**Форматирование даты и времени**

```
import datetime
today = datetime.datetime.today()
print(f"{today:%Y-%m-%d}")
# 2022-03-11
print(f"{today:%Y}")
# 2022
```
С помощью f-строк можно форматировать дату и время так, как если бы для этого использовался бы метод datetime.strftime. Это особенно приятно, когда понимаешь, что тут имеется больше возможностей форматирования значений, чем те немногие, которые упомянуты в документации. Так, Python-метод strftime поддерживает, кроме прочего, все способы форматирования значений, поддерживаемые его базовой реализацией на C. Эти возможности могут зависеть от платформы, именно поэтому в документации они не упоминаются. Но получается, что этими возможностями по форматированию значений, всё равно, можно воспользоваться. Например, можно применить спецификатор формата %F, являющийся эквивалентом %Y-%m-%d, или спецификатор %T, аналогичный %H:%M:%S. Стоит ещё упомянуть и о спецификаторах формата %x и %X, представляющих собой, соответственно, принятые в используемом языковом стандарте способы представления даты и времени. Использование этих возможностей форматирования значений, конечно, не ограничивается только f-строками. Полный список спецификаторов формата даты и времени можно найти в [Linux-справке по strftime](https://manpages.debian.org/bullseye/manpages-dev/strftime.3.en.html).

**Имена переменных и отладка**

Функционал f-строк сравнительно недавно (начиная с Python 3.8) дополнен возможностями по выводу имён переменных вместе с их значениями:

```
x = 10
y = 25
print(f"x = {x}, y = {y}")
# x = 10, y = 25
print(f"{x = }, {y = }")  # Лучше! (3.8+)
# x = 10, y = 25

print(f"{x = :.3f}")
# x = 10.000
```

Эта возможность называется «отладкой» («debugging»), её можно применять вместе с другими модификаторами. Она, кроме того, сохраняет пробелы, поэтому при обработке конструкций вида f»{x = }» и f»{x=}» получатся разные строки.

**Методы __repr__ и __str__**

Для формирования строковых представлений экземпляров классов по умолчанию используется метод __str__. Но если вместо этого метода нужно применить метод __repr__ — можно воспользоваться флагом преобразования !r:

```
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"User's name is: {self.first_name} {self.last_name}"

user = User("John", "Doe")
print(f"{user}")
# John Doe
print(f"{user!r}")
# User's name is: John Doe
```

Тут, внутри f-строки, можно было бы просто вызвать repr(some_var), но использование флага преобразования — это образец приятного стандартного и краткого решения подобной задачи.

**Отличная производительность**

За некие мощные возможности чего-либо и за «синтаксический сахар» часто приходится платить производительностью. Но в случае с f-строками это не так:

```
# python -m timeit -s 'x, y = "Hello", "World"' 'f"{x} {y}"'
from string import Template

x, y = "Hello", "World"

print(f"{x} {y}")  # 39.6 nsec per loop - Быстро!
print(x + " " + y)  # 43.5 nsec per loop
print(" ".join((x, y)))  # 58.1 nsec per loop
print("%s %s" % (x, y))  # 103 nsec per loop
print("{} {}".format(x, y))  # 141 nsec per loop
print(Template("$x $y").substitute(x=x, y=y))  # 1.24 usec per loop - Медленно!
```

Вышеприведённый код протестирован с помощью модуля timeit (python -m timeit -s 'x, y = «Hello», «World»' 'f»{x} {y}»'). Как видите, f-строки оказались самым быстрым из всех механизмов форматирования данных, которые даёт нам Python. Поэтому, даже если вы предпочитаете пользоваться другими средствами форматирования строк, рассмотреть возможность перехода на f-строки стоит хотя бы ради повышения производительности.

**Вся сила мини-языка спецификаций форматирования**

F-строки поддерживают мини-язык спецификаций форматирования Python. Поэтому в модификаторы, используемые в f-строках, можно внедрить множество операций форматирования данных:

```
text = "hello world"

# Центрирование текста:
print(f"{text:^15}")
# '  hello world  '

number = 1234567890
# Установка разделителя групп разрядов
print(f"{number:,}")
# 1,234,567,890

number = 123
# Добавление начальных нулей
print(f"{number:08}")
# 00000123
```

Мини-язык форматирования Python включает в себя гораздо больше, чем конструкции, рассчитанные на форматирование чисел и дат. Этот язык, кроме прочего, позволяет выравнивать или центрировать текст, добавлять к строкам начальные нули или пробелы, задавать разделители групп разрядов. Всем этим, конечно, можно пользоваться не только в f-строках, но и при применении других способов форматирования данных.

**Вложенные f-строки**

Если чьи-то нужды по форматированию данных не удаётся удовлетворить с помощью простых f-строк, можно прибегнуть к f-строкам, вложенным друг в друга:

```
number = 254.3463
print(f"{f'${number:.3f}':>10s}")
# '  $254.346'
```

Одни f-строки можно встраивать в другие f-строки, поступая так ради решения хитрых задач форматирования данных. Например — чтобы, как показано выше, добавить знак доллара к числу с плавающей точкой, выровненному по правому краю.

Вложенные f-строки могут применяться и в тех случаях, когда в спецификаторах формата нужно использовать переменные. Это, кроме прочего, способно улучшить читабельность кода с f-строками:

```
import decimal
width = 8
precision = 3
value = decimal.Decimal("42.12345")
print(f"output: {value:{width}.{precision}}")
# 'output:     42.1'
```

**Условное форматирование**

Взяв за основу предыдущий пример с вложенными f-строками, можно пойти немного дальше и воспользоваться во внутренних f-строках тернарными условными операторами:

```
import decimal
value = decimal.Decimal("42.12345")
print(f'Result: {value:{"4.3" if value < 100 else "8.3"}}')
# Result: 42.1
value = decimal.Decimal("142.12345")
print(f'Result: {value:{"4.2" if value < 100 else "8.3"}}')
# Result:      142
```

Подобные конструкции могут очень быстро стать нечитабельными. Поэтому, пользуясь ими, возможно, есть смысл разделять их на несколько строк кода.

**Лямбда-выражения**

Тот, кто хочет расширить границы возможностей f-строк, попутно взбесив тех, кто будет читать его код, может, приложив некоторые усилия, воспользоваться лямбда-выражениями:

```
print(f"{(lambda x: x**2)(3)}")
# 9
```

Скобки вокруг лямбда-выражения в данном случае обязательны. Это так из-за двоеточия, (:), которое, в противном случае, будет восприниматься системой как часть f-строки.

**Итоги**

Как видите, f-строки — это, и правда, весьма мощный механизм. Они обладают гораздо большими возможностями, чем думает большинство программистов. Основная часть этих «неизвестных» возможностей, правда, описана в документации по Python. Поэтому рекомендую читать документацию, причём — не только по f-строкам, но и по другим используемым вами модулям или возможностям Python. Углубление в документацию часто помогает обнаружить какие-то очень полезные вещи, которые не найти даже зарывшись в Stack Overflow.
