"""
Решено самостоятельно

Скорее всего show_last_message работает некорректно
"""
class Message:
    def __init__(self, text, fl_like: bool = False):
        self.text = text
        self.fl_like = fl_like

    def __repr__(self):
        return self.text


class Viber:
    __instance = None
    msgs = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def add_message(cls, msg: Message):
        cls.msgs += [msg]

    @classmethod
    def remove_message(cls, msg: Message):
        cls.msgs.remove(msg)

    @staticmethod
    def set_like(msg: Message):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, value: int):
        print(cls.msgs[-1:-(value) - 1])

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
# Viber.remove_message(msg)
print(msg.__dict__)
print(Viber.msgs)

