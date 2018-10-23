def get_lucky(list_numbers):
    """
    Проверка наличия цифры 7 в цифрах массива

    :param list_numbers:
    :return:
    """
    result = []

    for i in list_numbers:
        if "7" in str(i):
            result.append(i);

    return result


print(get_lucky([18, 3, 5, 7, 13, 14, 123, 4567]))
