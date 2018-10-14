from tempfile import mktemp
import os


class WrapStrToFile:
    """
    Вычисляемое свойство для записи и чтения файла
    """

    def __init__(self):
        self._filepath = mktemp()

    @property
    def content(self):
        return self._file_content()

    @content.setter
    def content(self, value):
        self._file_content(True, value)

    @content.deleter
    def content(self):
        if os.path.exists(self._filepath):
            os.unlink(self._filepath)

    def _file_content(self, write=False, content=''):
        file = None

        try:
            file = open(self._filepath, 'w' if write else 'r')

            if write:
                file.write(content)
            else:
                return file.read()

        except FileNotFoundError:
            return "Файл еще не существует"

        finally:
            if file:
                file.close()


wstf = WrapStrToFile()
print(wstf.content)

wstf.content = 'test str'
print(wstf.content)

wstf.content = 'text 2'
print(wstf.content)

del wstf.content
print(wstf.content)
