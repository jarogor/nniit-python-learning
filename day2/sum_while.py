def sum_while(list_numbers=[]):
    """
    Сумма всех элементов списка с помощью цикла while

    :param list_numbers:
    :return:
    """

    print('-' * 80)

    sum = 1
    count = len(list_numbers) - 1

    while count:
        sum = sum + list_numbers[count]
        count = count - 1

    print(f'Сумма всех чисел от 0 до {len(list_numbers)} с помощью цикла while: {sum}')
    print('-' * 80)


sum_while([i + 1 for i in range(100)])
