from time import time


def input_number(fn):
    """
    Декоратор обработки ввода числа
    """

    def wrap(input_value, message_error):
        try:
            return fn(int(input_value))
        except ValueError:
            return message_error

    return wrap


def timeit(fn):
    """
    Декоратор замера времени работы функции
    """

    def wrap(*args, **kwargs):
        time_start = time()
        result = fn(*args, **kwargs)
        time_end = time()

        print(f'Время выполнения функци: {time_end - time_start}')

        return result

    return wrap
