import threading
import random
import time


def compute(number):
    print("Начало {}".format(number))
    sleeping = random.randint(1, 5)
    time.sleep(sleeping)
    print("Конец {}, время {}".format(number, sleeping))


start = time.time()
threads = []

for i in range(5):
    thr = threading.Thread(target=compute, args=(i,))
    thr.start()
    threads.append(thr)

time.sleep(1)

for thr in threads:
    thr.join()

print("Общее время в секундах: {}".format(int(time.time() - start)))
