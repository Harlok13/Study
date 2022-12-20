"""
classmethod не особо и нужен с таким решением
Дублирование можно убрать с помощью наследования
Если делать по ТЗ, то валидацию имени можно делать
через set и проверять, что является подмножеством
"""
from re import fullmatch


class TextInput:
    def __init__(self, name, size=10):
        self.size = size
        if self.check_name(name):
            self.name = name
        else:
            raise ValueError("некорректное поле name")

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        return 50 >= len(name) >= 3 and fullmatch(r'^[a-zA-Z0-9А-Яа-яЁё ]{3,}$', name)


class PasswordInput:
    def __init__(self, name, size=10):
        self.name = None
        self.size = size
        if self.check_name(name):
            self.name = name

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 50 >= len(name) >= 3 and fullmatch(r'^[a-zA-Z0-9А-Яа-яЁё ]{3,}$', name):
            return True


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)
