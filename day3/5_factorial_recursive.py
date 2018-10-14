import sys

sys.path.append('.')

from decorators import *


def factorial_recursive(number):
    """
    Факториал числа вычисленный рекурсивно

    :param number:
    :return:
    """

    if number < 0:
        return "Число не натуральное"

    if number == 0:
        return 1

    return number * factorial_recursive(number - 1)


@input_number
@timeit
def get_number(n):

    if n < 0:
        return "Число не натуральное"

    if n == 0:
        return 1

    return factorial_recursive(n)


input_value = input("Введите целое натуральное число: ")
message_error = "[Ошибка]: Введённое значение не является числом."

print(get_number(input_value, message_error))
