from string import ascii_lowercase

ALPHABET = ascii_lowercase
# размер поля
MAX_WIDTH = MAX_HEIGHT = 25
MIN_WIDTH = MIN_HEIGHT = 5


game_table = {}

def create_table(width: int = MIN_WIDTH, height: int = MIN_HEIGHT):
    size_of_table(width, height)

    [print(f'{game_table.get(key)}|', end=' ')
     if num % width else print(f'{game_table.get(key)}\n')
     for i in range(width)
     for num, key in enumerate(game_table.keys(), 1)]



def size_of_table(width: int, height: int):
    """Создает словарь с игровыми ячейками"""
    if MAX_WIDTH >= width >= MIN_WIDTH and MAX_HEIGHT >= height >= MIN_HEIGHT:
        [game_table.setdefault(f'{char}{num}', 'X') for num in range(1, height+1)
         for char in ALPHABET[:width]]
    else:
        print(f'Размер поля должен быть в диапазоне [{MIN_WIDTH}, {MAX_WIDTH}]',
              f'Создано поле размером {MIN_WIDTH}х{MIN_HEIGHT}')
        size_of_table(10, 10)

create_table(5, 5)
print()
print(game_table)
