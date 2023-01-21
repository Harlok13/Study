from random import randint, choice
from operator import add, sub

RANGE_MAXIMUM = 99
OPERATORS = {'+': add,
             '-': sub}


def example_generator(range_maximum, operator):
    '''формирование примера'''
    answer = 0
    while 1 >= answer or answer >= range_maximum:
        operand_1 = randint(1, range_maximum)
        operand_2 = randint(1, range_maximum)
        answer = OPERATORS[operator](operand_1, operand_2)
    return f'{operand_1} {operator} {operand_2}', answer


def compiling_examples_list(quantity, range_maximum, operators):
    '''составление списка примеров'''
    return [example_generator(range_maximum, choice(list(operators))) for _ in range(quantity)]


def errors_output(erroneous_responses):
    '''вывод ошибочных ответов'''
    print()
    for example, correct_answer, response in erroneous_responses:
        response = 'некорректно' if response == 0 else f'"{response}"'
        print(f'в примере "{example}" правильный ответ "{correct_answer}", а ты ответил {response}')


def children_quiz(quantity=15, range_maximum=RANGE_MAXIMUM, operators=OPERATORS):
    '''взаимодействие с ребёнком'''
    examples_list = compiling_examples_list(quantity, range_maximum, operators)
    erroneous_responses = []
    for example, correct_answer in examples_list:
        try:
            response = int(input(f'введи ответ {example} '))
        except:
            response = 0
        if correct_answer != response:
            erroneous_responses.append((example, correct_answer, response))
    errors_output(erroneous_responses)


if __name__ == '__main__':
    children_quiz(3)
