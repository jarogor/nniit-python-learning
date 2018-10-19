import argparse
import os
from datetime import datetime


class CreateDateDir:
    """
    Утилитa создания по указанному пути директории с заданной датой в качестве названия
    """

    _root = 'day4'

    def __init__(self):
        parser = argparse.ArgumentParser(
            conflict_handler='resolve',
            add_help=False,
            description="Утилитa создания по указанному пути директории с заданной датой в качестве названия"
        )

        parser.add_argument('-h', '--help', action='help', help='Показывает данную справку')
        parser.add_argument('-y', action='store_true', help='Год', dest='year')
        parser.add_argument('-m', action='store_true', help='Месяц', dest='month')
        parser.add_argument('-d', action='store_true', help='День', dest='day')
        parser.add_argument('name', nargs='?', type=str)
        self._args = parser.parse_args()

    def _get_name_dir(self):
        name = []
        if self._args.year or self._args.month or self._args.day:
            if self._args.year:
                name.append(str(datetime.now().year))
            if self._args.month:
                name.append(str(datetime.now().month))
            if self._args.day:
                name.append(str(datetime.now().day))
        else:
            name.append('unknown')

        if self._args.name:
            return os.path.join(self._args.name, '-'.join(name))
        else:
            return os.path.join('.', self._root, '-'.join(name))

    def _mkdir(self, dirpath):
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        else:
            print("Директория уже существует")

    def run(self):
        self._mkdir(self._get_name_dir())


if __name__ == '__main__':
    create_date_dir = CreateDateDir()
    create_date_dir.run()
