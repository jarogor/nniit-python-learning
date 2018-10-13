def wave(name):
    """
    Создание списка вариантов введённой строки с одной прописной буквой в каждом

    :param name:
    :return:
    """

    name = name.lower()
    length = len(name) - 1
    result = []

    while length >= 0:
        result.append(name[:length] + name[length].upper() + name[length + 1:])
        length = length - 1

    return result


input_value = wave(input('Введите строку: '))

print(" ".join(input_value))
