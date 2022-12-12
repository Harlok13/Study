Для обращения к атрибутам класса мы можем использовать
имя класса, например: Person.type, и, как и атрибуты 
объекта, мы можем получать и изменять их значения.

Подобные атрибуты являются общими для всех объектов класса:
```
class Person:
     type = "Person"
     def __init__(self, name):
         self.name = name
 
 
tom = Person("Tom")
bob = Person("Bob")
print(tom.type)     # Person
print(bob.type)     # Person
 
# изменим атрибут класса
Person.type = "Class Person"
print(tom.type)     # Class Person
print(bob.type)     # Class Person
```
Атрибуты класса могут применяться для таких ситуаций,
когда нам надо определить некоторые общие данные для
всех объектов. Например:

```
class Person:
    default_name = "Undefined"
 
    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = Person.default_name
 
 
tom = Person("Tom")
bob = Person("")
print(tom.name)  # Tom
print(bob.name)  # Undefined
```
В данном случае атрибут `default_name` хранит имя по
умолчанию. И если в конструктор передана пустая строка для 
имени, то атрибуту name передается значение атрибута
класса `default_name`. Для обращения к атрибуту класса внутри
методов можно применять имя класса

	
`self.name = Person.default_name`

### Атрибут класса

Возможна ситуация, когда атрибут класса и атрибут объекта 
совпадает по имени. Если в коде для атрибута объекта не 
задано значение, то для него может применяться значение
атрибута класса:

```
class Person:
    name = "Undefined"
 
    def print_name(self):
        print(self.name)
 
 
tom = Person()
bob = Person()
tom.print_name()    # Undefined
bob.print_name()    # Undefined
 
bob.name = "Bob"
bob.print_name()    # Bob
tom.print_name()    # Undefined
```
Здесь метод `print_name` использует атрибут объект
`name`, однако нигде в коде этот атрибут не устанавливается.
Зато на уровне класса задан атрибут `name`. Поэтому 
при первом обращении к методу `print_name`, в нем будет 
использоваться значение атрибута класса:

```
tom = Person()
bob = Person()
tom.print_name()    # Undefined
bob.print_name()    # Undefined
```
Однако далее мы можем поменять установить атрибут объекта:
```
bob.name = "Bob"
bob.print_name()    # Bob
tom.print_name()    # Undefined
```
Причем второй объект - `tom` продолжит использовать атрибут
класса. И если мы изменим атрибут класса, соответственно
значение `tom.name` тоже изменится:
```
tom = Person()
bob = Person()
tom.print_name()    # Undefined
bob.print_name()    # Undefined
 
Person.name = "Some Person"     # меняем значение атрибута класса
bob.name = "Bob"                # устанавливаем атрибут объекта
bob.print_name()    # Bob
tom.print_name()    # Some Person
```
