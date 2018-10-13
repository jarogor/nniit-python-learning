from time import sleep
from random import randint


class Man:
    first_name = "<Unknown>"

    def __init__(self, first_name):
        self.first_name = first_name

    def solve_task(self):
        print(f"{self.first_name} said:")
        print("I'm not ready yet")

    def get_first_name(self):
        return self.first_name


class Pupil(Man):
    def __init__(self, first_name):
        super().__init__(first_name)

    def solve_task(self):
        print('thinking...')
        sleep(randint(3, 6))
        super().solve_task()


input_value = input("Введите имя: ")
pupil = Pupil(input_value)

pupil.solve_task()
