"""Eugene S."""
import random as rnd


NUMBER_OF_EXERCISES = 15
NUMBER_MIN_LIMIT = 0
NUMBER_MAX_LIMIT = 100


def addition():
    num1 = rnd.randint(NUMBER_MIN_LIMIT, NUMBER_MAX_LIMIT)
    num2 = rnd.randint(NUMBER_MIN_LIMIT, NUMBER_MAX_LIMIT - num1)
    return f"{num1} + {num2} = ", num1 + num2


def subtraction():
    num1 = rnd.randint(NUMBER_MIN_LIMIT, NUMBER_MAX_LIMIT)
    num2 = rnd.randint(NUMBER_MIN_LIMIT, NUMBER_MAX_LIMIT)
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    return f"{max_num} - {min_num} = ", max_num - min_num


def get_user_solution(exercise):
    print(exercise, end='')
    user_solution = input()
    while not user_solution.isdecimal():
        print("Ошибка: Нужно ввести число. Попробуй еще раз.")
        print(exercise, end='')
        user_solution = input()
    return int(user_solution)


def check_user_solution(exercise, solution):
    print("-------------Реши пример:--------------------")
    user_solution = get_user_solution(exercise)
    while user_solution != solution:
        print("Ошибка: Неверный ответ. Попробуй еще раз.")
        user_solution = get_user_solution(exercise)
    print("Верно!")


def main():
    exercises = (subtraction, addition)
    for _ in range(NUMBER_OF_EXERCISES):
        exercise, solution = rnd.choice(exercises)()
        check_user_solution(exercise, solution)
    print("---------------------------------------------")
    print("Поздравляю! Все примеры решены.")


if __name__ == '__main__':
    main()
