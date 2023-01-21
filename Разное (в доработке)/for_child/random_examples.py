from pprint import pprint
from random import randint, choice, seed
from operator import add, sub


def create_random_examples(count: int, seed_val: int = None) -> list[str]:
    """Создает список из рандомных примеров, результат которых в диапазоне [1, 100]"""
    if seed_val: seed(seed_val)
    operators = {'+': add, '-': sub}
    lst_of_examples = []
    count_of_examples = 0
    while count_of_examples <= count:
        operand_1, operand_2, operator = randint(1, 100), randint(1, 100), choice(('-', '+'))
        if 0 <= operators.get(operator)(operand_1, operand_2) <= 100:
            lst_of_examples.append(f'{operand_1} {operator} {operand_2} = ')
            count_of_examples += 1

    return lst_of_examples


if __name__ == '__main__':
    pprint(create_random_examples(15))
    pprint(create_random_examples(20, 2))
