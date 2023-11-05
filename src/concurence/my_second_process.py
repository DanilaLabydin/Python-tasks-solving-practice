import multiprocessing
import time
import os


def whoami(name):
    print("I am %s, in process %s" % (name, os.getpid()))


def loopy(name):
    whoami(name)
    start = 1
    stop = 10000000
    for num in range(start, stop):
        print(f"\tNumber {num} of {stop}. Honk!")
        time.sleep(1)

def second_loopy(name):
    whoami(name)
    while True:
        print("SECOND PROCESS!!!!!!!")
        print(time.sleep(1))


if __name__ == "__main__":
    whoami("main")

    process1 = multiprocessing.Process(target=loopy, args=("loppy",))
    process2 = multiprocessing.Process(target=second_loopy, args=("second_loppy",))
    process1.start()
    process2.start()
    time.sleep(5)
    process1.terminate()
    process2.terminate()
