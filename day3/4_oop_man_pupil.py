from time import sleep
from random import randint


class Man:
    name = "<Unknown>"

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print(f"{self.name} said:")
        print("I'm not ready yet")

    def get_name(self):
        return self.name


class Pupil(Man):
    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        print('thinking...')
        sleep(randint(3, 6))
        super().solve_task()


input_value = input("Введите имя: ")
pupil = Pupil(input_value)

pupil.solve_task()
