import sys

sys.path.append('.')

from decorators import *


@input_number
@timeit
def factorial_loop(number):
    """
    Факториал числа вычисленный в цикле

    :param number:
    :return:

    """
    if number < 0:
        return "Число не натуральное"

    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    return factorial


input_value = input("Введите целое натуральное число: ")
message_error = "[Ошибка]: Введённое значение не является числом."

print(factorial_loop(input_value, message_error))
