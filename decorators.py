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

    def wrap(*args):
        start_time = time()
        fn(*args)
        print(f'Время выполнения функци: {time() - start_time}')

    return wrap
