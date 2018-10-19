import itertools


def merge(*args):
    """
    Слияние списков

    :param args:
    :return:
    """
    return list(itertools.chain.from_iterable([i for i in args]))


def str_length(l):
    """
    Фильтрация списка строк

    :param l:
    :return:
    """
    return list(itertools.filterfalse(lambda x: not len(x) >= 5, l))


def str_combination(string):
    """
    Перебор комбинаций

    :param string:
    :return:
    """
    return list(itertools.permutations(string, 4))


print(merge([1, 2, 3], [4, 5], [6, 7]))
print(str_length(['hello', 'i', 'write', 'cool', 'code']))
print(str_combination('password'))
