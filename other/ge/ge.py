from adventurelib import *


class Person:
    """Game character"""
    __hero_count = 0

    def __new__(cls, *args, **kwargs):
        """Limit to create only one character"""
        if not cls.__hero_count:
            cls.__hero_count = 1
            return super(Person, cls).__new__(cls)
        else:
            print('There should be only one hero')

    def __init__(self, health: int = 100, armor: int = 0, attack: int = 6, lvl: int = 1):
        self._hero_health = health
        self._hero_armor = armor
        self._hero_attack = attack
        self._hero_lvl = lvl


class Equipment:
    pass

start()
hero = Person()
hero1 = Person()
print(hero.__dict__)
# print(hero1)
