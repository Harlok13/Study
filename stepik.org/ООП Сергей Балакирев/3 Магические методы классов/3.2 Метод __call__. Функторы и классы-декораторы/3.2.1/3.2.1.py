import random


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join(random.choices(self.psw_chars,
                       k=random.randint(self.min_length, self.max_length)))


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
print(rnd())

lst_pass = [rnd() for _ in range(3)]
print(lst_pass)
