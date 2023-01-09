from math import floor


def calculate_expression(func):
    operands = {'plus': '+', 'minus': '-', 'times': '*', 'divided_by': '/'}

    def wrapper(operand=None):
        if operand is not None:
            expression = operands.get(operand.split()[0]) + operand.split()[1]
            if expression.startswith('/'):
                return floor(eval(f'{func()} {expression}'))
            else:
                return eval(f'{func()} {expression}')

        return func()

    return wrapper


plus = lambda var: f'plus {var}'
minus = lambda var: f'minus {var}'
times = lambda var: f'times {var}'
divided_by = lambda var: f'divided_by {var}'


@calculate_expression
def zero(operand=None):
    return 0


@calculate_expression
def one(operand=None):
    return 1


@calculate_expression
def two(operand=None):
    return 2


@calculate_expression
def three(operand=None):
    return 3


@calculate_expression
def four(operand=None):
    return 4


@calculate_expression
def five(operand=None):
    return 5


@calculate_expression
def six(operand=None):
    return 6


@calculate_expression
def seven(operand=None):
    return 7


@calculate_expression
def eight(operand=None):
    return 8


@calculate_expression
def nine(operand=None):
    return 9


if __name__ == '__main__':
    print(zero(plus(six())))
    print(five(divided_by(two())))
    print(nine(times(zero())))
    print(eight(plus(seven())))

    assert zero(plus(six())) == 6, f'{zero(plus(six()))}'
    assert five(divided_by(two())) == 2, f'{five(divided_by(two()))}'
    assert nine(times(zero())) == 0, f'{nine(times(zero()))}'
    assert eight(plus(seven())) == 15, f'{eight(plus(seven()))}'

"""
 ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
    ⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
    ⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
    ⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
    ⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
    ⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
    ⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
    ⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼
    ⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
    ⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
    ⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
    ⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
    ⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉
    ⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄
"""

"""
operands = {'plus': '+', 'minus': '-', 'times': '*', 'divided_by': '/'}
def zero(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'0 {expression}')
    return 0
def one(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'1 {expression}')
    return 1
def two(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'2 {expression}')
    return 2
def three(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'3 {expression}')
    return 3

def four(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'4 {expression}')
    return 4
def five(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'5 {expression}')
    return 5
def six(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'6 {expression}')
    return 6
def seven(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'7 {expression}')
    return 7
def eight(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'8 {expression}')
    return 8
def nine(operand=None):
    if operand:
        expression = operands.get(operand.split()[0]) + operand.split()[1]
        return eval(f'9 {expression}')
    return 9

def plus(var): return f'plus {var}'
def minus(var): return f'minus {var}'
def times(var): return f'times {var}'
def divided_by(var): return f'divided_by {var}'
"""
