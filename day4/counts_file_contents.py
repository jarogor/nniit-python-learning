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
        return len(self._get_file().readlines())

    def count_words(self):
        return len(self._get_file().read().split())

    def count_integers(self):
        content = self._get_file().read().split()
        count = []
        for i in content:
            if i.isnumeric():
                count.append(i)

        return len(count)

    def printer(self):
        print("Чисел в файле: {}".format(self.count_integers()))
        print("Строк в файле: {}".format(self.count_lines()))
        print("Слов в файле: {}".format(self.count_words()))

    def _get_file(self):
        try:
            if os.path.exists(self._filepath):
                return open(self._filepath, 'r')

        except FileNotFoundError:
            return "Файл не существует"


file = File('day4/example.txt')
file.printer()
