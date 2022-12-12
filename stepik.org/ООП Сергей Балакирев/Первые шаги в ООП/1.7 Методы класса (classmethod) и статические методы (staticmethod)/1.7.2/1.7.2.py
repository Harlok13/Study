from string import ascii_lowercase, digits

class TextInput:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class PasswordInput:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
