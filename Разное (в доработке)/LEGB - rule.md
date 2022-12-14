## LEGB - rule
* L - local
* E - enclosed
* G - global
* B - builtins

```
import builtins

builtins.scope = 'builtins'

scope = 'global'

def outer():
    scope = 'enclosed'
    def inner():
        scope = 'local'
        
    inner()
    
if __name__ == '__main__':
    outer()
```
Функция `outer` вызовет функцию `inner` и распечатает нам 
`scope`, а именно - `local` и дальше он искать не будет.
Но если закомментировать эту строчку, то он найдет `scope` уже 
в функции `outer`, а значит на экран выведет `enclosed`.
Тоже самое будет, если и в `outer` закомментировать `scope`. 
В этом случае будет найден глобальный `scope`.

**Вывод**\
Интерпретатор всегда будет искать переменные, которые находятся 
в том пространстве имен, в котором в данный момент исполняется код
и только после этого, если переменная не будет найдена, он будет 
подниматься наверх как по лестнице и искать в следующем пространстве имен.
В противном случае будет выкинута ошибка


**Еще один момент**
```
max = 10


def outer():
    def inner():
        print(max([1, 2, 3]))
        
    inner()
    
if __name__ == '__main__':
    outer()
```
Если в глобальном пространстве будет объявлена
переменная с именем функции (в нашем случае `max`), то в функции `inner`
не будет вызвана функция `max` из `builtins`, потому что интерпретатор
пойдет искать ее в других пространствах имен
