"""
В зависимости от значения переменной TYPE_OS
создается объект либо класса DialogWindows, либо
DialogLinux
"""

TYPE_OS = 0  # 1 - Windows; 2 - Linux


class Dialog:

    def __new__(cls, *args, **kwargs):
        if TYPE_OS:
            return super().__new__(DialogWindows)
        elif TYPE_OS != 1:
            return super().__new__(DialogLinux)

    def __init__(self, name):
        self.name = name


class DialogWindows(Dialog):
    name_class = "DialogWindows"


class DialogLinux(Dialog):
    name_class = "DialogLinux"


dlg = Dialog('винда')
print(dlg)
