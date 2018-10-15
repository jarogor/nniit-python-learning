def wave(name):
    """
    Создание списка вариантов введённой строки с одной прописной буквой в каждом

    :param name:
    :return:
    """

    name = name.lower()
    index = len(name) - 1
    result = []

    while index >= 0:
        result.append(name[:index] + name[index].upper() + name[index + 1:])
        index = index - 1

    return result


input_value = wave(input('Введите строку: '))

print(" ".join(input_value))
