from time import time


class TimeManager:
    """
    Менеджер контекста замеряющий время
    """

    start = 0

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Имя модуля: {}".format(__name__))
        print("Время выполнения: {}".format(time() - self.start))

