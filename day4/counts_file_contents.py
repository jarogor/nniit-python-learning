import os
import sys

sys.path.append('.')


class File:
    """
    Подсчёт слов, строк и чисел в файле
    """

    def __init__(self, filepath):
        self._filepath = filepath

    def count_lines(self):
        length = len(self._file().readlines())
        self._file().close()

        return length

    def count_words(self):
        length = len(self._file().read().split())
        self._file().close()

        return length

    def count_integers(self):
        content = self._file().read()
        count = []
        for i in content:
            if i.isnumeric():
                count.append(i)

        return len(count)

    def _file(self):
        try:
            if os.path.exists(self._filepath):
                return open(self._filepath, 'r')

        except FileNotFoundError:
            return "Файл не существует"

    def printer(self):
        print("Чисел в файле: {}".format(self.count_integers()))
        print("Строк в файле: {}".format(self.count_lines()))
        print("Слов в файле: {}".format(self.count_words()))


file = File('day4/example.txt')
file.printer()
