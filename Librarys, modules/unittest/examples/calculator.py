# написать функцию калькулятор, которая принимает на вход строку, содержащую два целых числа один арифметический знак
# операции + - / * возвращает результат выполнения этой операции. Если числа не целые или нет знака операции, то
# бросать исключение ValueError
from operator import add, mul, sub, truediv


def calculator(expression: str):
    """
    Принимает строку с двумя числами и оператором.
    Проверяет наличие оператора в строке, иначе бросает исключение.
    При положительной валидации делит строку по оператору и вычисляет значение,
    в противном случае бросает исключение.
    """
    allowed = {'+': add, '*': mul, '-': sub, '/': truediv}
    valid_operator = [key for key in allowed if key in expression]
    if not any(valid_operator):
        raise ValueError(f'Выражение должно содержать хотя бы один знак  {*allowed.keys(),}')

    if valid_operator:
        operator = valid_operator[0]
        try:
            left, right = expression.split(operator)
            left, right = int(left), int(right)
            return allowed.get(operator)(left, right)

        except (ValueError, TypeError):
            raise ValueError('Выражение должно содержать 2 целых числа и один оператор')

if __name__ == '__main__':
    print(calculator('3-5'))
    print(calculator('4+3'))
