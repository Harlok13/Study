"""
Решено самостоятельно
"""


class Application:
    def __init__(self, name: str, blocked=False):
        self.name = name
        self.blocked = blocked


class AppStore:
    __instance = None
    apps = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

    @classmethod
    def add_application(cls, app: Application):
        cls.apps += [app]

    @classmethod
    def remove_application(cls, app: Application):
        cls.apps.remove(app)

    @staticmethod
    def block_application(app: Application):
        app.blocked = True

    @classmethod
    def total_apps(cls) -> int:
        return len(cls.apps)


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.apps)
# store.remove_application(app_youtube)
