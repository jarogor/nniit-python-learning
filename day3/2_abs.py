import sys

sys.path.append('.')

from decorators import input_number


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
message_error = "[Ошибка]: Введённое значение не является числом."

print(custom_abs(input_value, message_error))
