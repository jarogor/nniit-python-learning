from time import sleep
from random import random
from cm_timeit import TimeManager


with TimeManager():
    sleep(random())
    print("Имя модуля: {}".format(__name__))
