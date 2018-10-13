import sys

sys.path.append('.')

from helper import input_number


@input_number
def custom_abs(x):
    """
    Модуль числа

    :param x:
    :return:
    """

    if x < 0:
        return x * -1
    else:
        return x


input_value = input("Введите целое число: ")
print(custom_abs(input_value, "[Ошибка]: Введённое значение не является числом."))
