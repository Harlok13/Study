class Clock:

    def __check_time(self, tm):
        return type(self.__time) == int and 0 <= tm < 10_000

    def __init__(self, time):
        self.__time = 0
        if self.__check_time(time):
            self.__time = time

    def set_time(self, tm: int):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


clock = Clock(4530)
clock.set_time(1000000)
print(clock.get_time())
