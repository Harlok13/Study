class Server:
    __IP = 0
    buffer = []

    def __new__(cls, *args, **kwargs):
        cls.__IP += 1
        return super().__new__(cls)

    def __init__(self):
        self.IP = self.__IP

    def send_data(self, data):
        pass


    def clean_data(func):

        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            cls.buffer = []
            return res

        return wrapper

    @clean_data
    @classmethod
    def get_data(cls):
        return cls.buffer

    def get_ip(self):
        pass


class Router:
    buffer = []

    def link(self, server: Server):
        pass

    def unlink(self, server: Server):
        pass

    def send_data(self):
        pass


class Data:
    def __init__(self, data: str, ip: Server):
        self.data = data
        self.ip = ip
