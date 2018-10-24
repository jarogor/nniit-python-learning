def pi(i):
    """
    Вычисление Пи

    :param i:
    :return:
    """
    result = 4.0
    x = 3.0

    # 4 - 4/3 + 4/5 - 4/7 + 4/9 ...
    while x < i:
        result = result - (4 / x) + (4 / (x + 2))
        x += 4

    return result


print(pi(1000000))
