import multiprocessing
import datetime
import time
import random


def get_time():
    sleep_seconds = random.randint(1, 10)
    time.sleep(sleep_seconds)
    print(datetime.datetime.now(), sleep_seconds)


if __name__ == "__main__":
    process1 = multiprocessing.Process(target=get_time)
    process2 = multiprocessing.Process(target=get_time)
    process3 = multiprocessing.Process(target=get_time)

    process1.start()
    process2.start()
    process3.start()

