def sum_for(list_numbers=[]):
    """
    Сумма всех элементов списка с помощью цикла for

    :param list_numbers:
    :return:
    """

    print('-' * 80)

    sum = 0

    for number in list_numbers:
        sum = sum + number

    print(f'Сумма всех чисел от 0 до {number} с помощью цикла for: {sum}')
    print('-' * 80)


sum_for([i + 1 for i in range(100)])
