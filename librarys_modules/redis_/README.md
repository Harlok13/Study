# REDIS

### Список распростаненных команд
**[`SET`](#)**\
**[`GET`](#)**\
**[`EXISTS`](#)**\
**[`FLUSHALL`](#)**\
**[`GETSET`](#)**\
**[`DEL`](#)**\
**[`APPEND`](#)**\
**[`KEYS`](#)**\
**[`INCR/DECR`](#)**\
**[`TTL`](#)**\
**[`PERSIST`](#)**\
**[`RENAME`](#)**

### SET
Команда используется для установки ключа и его значения, с дополнительными
необязательными параметрами для указания срока действия записи значения ключа.
Давайте установим ключ foo со значением «hello world». Параметр EX указывает 
время жизни объекта в секундах, PX в милисекундах:
```
127.0.0.1:6379> SET foo "hello world"
OK

127.0.0.1:6379> SET foo1 "hello world" ex 5
OK
```

### GET
Команда используется для получения значения, связанного с ключом. Если запись
значения ключа превысила срок действия, будет возвращено nil:
```
127.0.0.1:6379> GET foo
"hello world"

# если истечет время жизни записи
127.0.0.1:6379> GET foo
(nil)
```

### EXISTS
Эта команда проверяет, существует ли что то с данным ключом. Она возвращает
1 если объект существует или 0 если нет. Boolean типа в Redis нет.
```
127.0.0.1:6379> EXISTS foo
(integer) 1
```

### FLUSHALL
Эта команда полностью удаляет все данные в текущем сеансе.

### GETSET
Команда возвращает текущее значение и устанавливает новое. Используется для
атомарного управления данными.
```
127.0.0.1:6379> SET foo "hello"
OK
127.0.0.1:6379> GETSET foo "world"
"hello"
127.0.0.1:6379> GET foo
"world"
```

### DEL
Команда удаляет ключ и соответствующее значение:
```
127.0.0.1:6379> DEL foo
(integer) 1
```

### APPEND
Команда добавляем в соотвествующий ключ дополнительное значение. Возвращает
количество символов итогового значения.
```
127.0.0.1:6379> SET foo "hello"
OK
127.0.0.1:6379> APPEND foo " world"
(integer) 11
127.0.0.1:6379> GET foo
"hello world"
```

### KEYS
Возвращает все ключи из базы по указанному шаблону. Есть предостережение
что в реальных приложения эту команду лучше не использовать из-за того что
она очень медленная.
```
127.0.0.1:6379> KEYS *
1) "boo"
2) "foo"
```

### INCR/DECR
Инкремент / декримент. Если значение ключа integer (хотя в базе храниться
все равно строка) можно увеличить или уменьшить значение на 1. Если
использовать команду INCR с несуществующем значением то создаться новый
ключ со значением 1.
```
127.0.0.1:6379> SET foo 1
OK
127.0.0.1:6379> INCR foo
(integer) 2
127.0.0.1:6379> INCR foo
(integer) 3
127.0.0.1:6379> DECR foo
(integer) 2
```

### TTL
Когда ключ установлен с истечением срока действия (например SET foo EX 10), 
эту команду можно использовать для просмотра оставшегося времени:
```
127.0.0.1:6379> SET foo 10 EX 10
OK
127.0.0.1:6379> TTL foo
(integer) 6
127.0.0.1:6379> TTL foo
(integer) 5
127.0.0.1:6379> TTL foo
(integer) 2
127.0.0.1:6379> TTL foo
(integer) -2
```

### PERSIST
Если мы передумаем об истечении срока действия ключа, мы можем использовать
эту команду, чтобы удалить период истечения срока действия:
```
127.0.0.1:6379> PERSIST foo
(integer) 1

127.0.0.1:6379> TTL foo
(integer) -1

127.0.0.1:6379> GET foo
"bar"
```

### RENAME
Эта команда используется для переименования ключей на нашем сервере Redis:
```
127.0.0.1:6379> RENAME foo foo2
OK

127.0.0.1:6379> GET foo
(nil)

127.0.0.1:6379> GET foo2
"bar"
```

### HSET
**ХЕШ ТАБЛИЦЫ**\
Redis позволяет в качестве значения так же использовать ключ: значение. 
Что по сути будет почти аналогией объектов из JavaScript или словари в
Python. Для записи объекта используется команда HSET в следующем формате
HSET имя_ключа имя_атрибута значение. Для чтения объекта используется
команда HGET в формате HGET имя_ключа имя_атрибута. Команда HGETALL 
используется для получения
```
127.0.0.1:6379> HSET obj attr1 value1
(integer) 1
127.0.0.1:6379> HSET obj attr2 value2
(integer) 1
127.0.0.1:6379> HGET obj attr1
"value1"
127.0.0.1:6379> HGETALL obj
1) "attr1"
2) "value1"
3) "attr2"
4) "value2"
```

### SADD
**МНОЖЕСТВА**\
Не упорядоченная коллекция уникальных элементов. Аналог set в Python.
Для добавление нового элемента во множество используется команда SADD.
Для получения все элементов используется команда SMEMBERS. SUNION 
используется для объединение множеств. SDIFF используется для вычитания 
из первого множества второго. SINTER возвращает общие элементы указаных
множеств. SPOP удаляет и возвращает случайный элемент множества.
```
127.0.0.1:6379> SADD objects obj1
(integer) 1
127.0.0.1:6379> SADD objects obj2
(integer) 1
127.0.0.1:6379> SADD objects obj3
(integer) 1
127.0.0.1:6379> SADD objects obj1
(integer) 0
127.0.0.1:6379> SMEMBERS objects
1) "obj2"
2) "obj3"
3) "obj1"
```

### ZADD
**УПОРЯДОЧЕННЫЕ МНОЖЕСТВА**\
Упорядоченная коллекция уникальных элементов. Для добавление нового элемента
в упорядоченное множество используется команда ZADD. Формат ZADD имя_ключа 
порядковое_число_упорядочивания_множества значение\
Команда ZRANGE возвращает срез данных множества

### LPUSH LRANGE LPOP
**УПОРЯДОЧЕННЫЕ МНОЖЕСТВА**\
Список это последовательность значений упорядоченных по порядку их создания.
Аналог двух-стороннего стека (то есть стека в который можно добавлять с двух
сторон). Списки обычно применяются для создания очередей.\
Команда добавления элемента в список LPUSH/
LRANGE — возвращает срез списка с левой стороны. Формат LRANGE имя_списка
индекс_начало индекс_конца Указание -1 означает до конца списка.\
LPOP — вернуть одно значение c левой стороны и удалить его из списка. 
Формат LPOP имя_списка. Аналогичные команды RPUSH, RRANGE, RPOP только
для правой стороны.
```
127.0.0.1:6379> LPUSH obj1 value1
(integer) 1
127.0.0.1:6379> LPUSH obj1 value2
(integer) 2
127.0.0.1:6379> LPUSH obj1 value3
(integer) 3
127.0.0.1:6379> LRANGE obj1 0 -1
1) "value3"
2) "value2"
3) "value1"
127.0.0.1:6379> 
```

### Транзакции
Обычное определение транзакций для реляционных баз данных означает следующее: 
транзакции это группа команд с базой данных, которые должны либо полностью 
выполнится или в случае возникновение ошибки вернуть состояние базы данных
в исходное состояние. В Redis то же есть такое понятие как транзакции. Но 
означает немного другое. Транзакции в Redis это просто последовательное
выполнение ранее записаных команд без возможности полноценного возвращения 
исходного состояния в случае ошибки исполнения.

С помощью команды MULTI можно начать запись команд. Далее введенные команды
не исполняются а записываются в буфер. Это будет происходит до ввода команды
на исполнения транзакции EXEC. Далее все ранее введенные команды будут 
исполнены один за другим. Команда DISCARD отмена записи команд транзакций.
Если возникнет ошибка в процессе ввода команд вся транзакция не будет
выполнена.
```
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379> SET obj1 value1
QUEUED
127.0.0.1:6379> SET obj2 value2
QUEUED
127.0.0.1:6379> EXEC
1) OK
2) OK
127.0.0.1:6379> GET obj1
"value1"
```
