def e(number):
    """
    Вычисление числа Эйлера
    """

    result = 1
    factorial = 1
    count = 1

    while count <= number:
        factorial = count * factorial
        result += 1 / factorial
        count += 1
    
    return result

print(e(100))
