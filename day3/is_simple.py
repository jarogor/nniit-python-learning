import sys

sys.path.append('.')

from helper import input_number


@input_number
def is_simple(x):
    """
    Является ли число простым

    :param x:
    :return:
    """

    if x <= 0:
        return "Число не натуральное"

    if x == 1:
        return "Число простое"

    if not all([x % i for i in range(2, x)]):
        return "Число не простое"

    return "Число простое"


input_value = input("Введите натуральное число: ")
message_error = "[Ошибка]: Введённое значение не является числом."

print(is_simple(input_value, message_error))
