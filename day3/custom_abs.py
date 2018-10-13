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


while True:
    input_value = input("Введите целое число: ")

    try:
        print(f'Модуль числа {input_value}: {custom_abs(int(input_value))}')
        break

    except ValueError:
        print("[Ошибка]: Введённое значение не является числом.")
