def input_number(callback):
    """
    Декоратор обработки ввода числа
    """

    def wrap(input_value, message_error):
        try:
            return callback(int(input_value))
        except ValueError:
            return message_error

    return wrap
