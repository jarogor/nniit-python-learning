def custom_enumerate(x):
    """
    Создает объект, который генерирует кортежи,
    состоящие из двух элементов —
    индекса элемента и самого элемента

    :param x:
    :return:
    """

    try:
        iterator = iter(x)
    except TypeError as er:
        print(f'{x} is not iterable')
        return

    index = 0

    for i in iterator:
        if isinstance(x, dict):
            yield (index, {i: x[i]})
        else:
            yield (index, i)
        index += 1


print("\nList:")
l = [1, 2, 'qwe', 'rty', 4]
for i, j in custom_enumerate(l):
    print(i, j)

print("\nTuple:")
t = (1, 2, 3)
for i, j in custom_enumerate(t):
    print(i, j)

print("\nDict:")
d = {'qwe': 'rty', 1: 123, 23: 456}
for i, j in custom_enumerate(d):
    print(i, j)

print("\nString:")
s = 'qwerty'
for i, j in custom_enumerate(s):
    print(i, j)

print("\nSet:")
st = set(l)
for i, j in custom_enumerate(st):
    print(i, j)

print("\nInt:")
for i, j in custom_enumerate(123):
    print(i, j)
