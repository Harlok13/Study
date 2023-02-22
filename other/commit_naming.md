# Commit naming

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
```

- chore: рутина, обслуживание кода, невидимое пользователю (например изменения .gitignore)
- feat: новая функциональность
- fix: исправление багов
- build: изменения, связанные со сборкой проекта (например, работа с библиотеками npm)
- perf: код, который улучшает производительность
- ref: рефакторинг, код, который не относится к добавлению новых функций или исправлению ошибок
- test: создание новых тестов или изменение существующих
- style: - исправляем опечатки, исправляем форматирование
- docs: - всё, что касается документации
- study: - код, написанный в учебных целях (чтобы отработать какой-то материал)

Общий стиль:  
действие (с маленькой буквы) + для какой сущности + (необязательно подробности)  

На английском:  
fix NoMethodError in RemoteReader  

Например:  
fix(lynx): fix NoMethodError in RemoteReader  
docs(all): provide README.md with "Commit messages" section  
style(csv): исправление форматирования в bin/csv2json  

## Credits

Взято из github пользователя __[`Voko`](https://gist.github.com/Aleksey-Voko)__

## Дополнительно (p.s. сторонний ресурс)
* [Правила написания коммитов](https://habr.com/ru/post/416887/)