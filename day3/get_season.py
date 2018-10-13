import sys

sys.path.append('.')

from helper import input_number


def get_season(num):
    seasons = ['Зима', 'Весна', 'Лето', 'Осень']
    return seasons[num]


@input_number
def get_month(num=1):
    """
    Время года по номеру месяца

    :param num:
    :return:
    """
    if 1 <= num <= 12:
        if num == 12:
            return get_season(0)
        else:
            return get_season(num // 3)
    else:
        return "Как ни странно, но в году всего 12 месяцев."


print(get_month(input("Введите номер месяца: "), "Номер месяца должен быть числом"))
