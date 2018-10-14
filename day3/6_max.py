def custom_max(x, *args):
    """
    Возвращает максимальное значение из множества

    :param x:
    :param args:
    :return:
    """

    max_value = 0

    if len(args):
        enum = args
    else:
        enum = x

    for i in enum:
        if i > max_value:
            max_value = i

    return max_value


print(custom_max([45, 2, 7, 89, 61, 14, 11, 3]))
print(custom_max(45, 2, 7, 89, 61, 14, 11, 3))
