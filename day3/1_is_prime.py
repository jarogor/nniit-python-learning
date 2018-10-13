import sys

sys.path.append('.')

from decorators import input_number


@input_number
def is_prime(x):
    """
    Является ли число простым

    :param x:
    :return:
    """

    if x <= 0:
        return "Число не натуральное"

    if x > 1000:
        return "Число слишком большое"

    if x == 1:
        return "Число простое"

    if not all([x % i for i in range(2, x)]):
        return "Число не простое"

    return "Число простое"


input_value = input("Введите натуральное число от 0 до 1000: ")
message_error = "[Ошибка]: Введённое значение не является числом."

print(is_prime(input_value, message_error))
