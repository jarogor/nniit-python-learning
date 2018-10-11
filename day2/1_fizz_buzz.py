def fizz_buzz(list_numbers=[]):
    """
    fizz_buzz

    Выводит на экран в случае кратности
     - трём -- слово Fizz
     - пяти -- слово Buzz
     - пятнадцати -- слово FizzBuzz

    :param list_numbers:
    :return:
    """

    print('-' * 80)
    print('FizzBuzz')

    for number in list_numbers:
        if not number:
            continue

        if number % 15 == 0:
            print(f'{number}:\t FizzBuzz')
            continue

        if number % 3 == 0:
            print(f'{number}:\t Fizz')

        if number % 5 == 0:
            print(f'{number}:\t Buzz')

    print('-' * 80)


fizz_buzz([i + 1 for i in range(100)])
