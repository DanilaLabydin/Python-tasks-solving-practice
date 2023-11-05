import multiprocessing
import os


def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))


if __name__ == "__main__":
    whoami("I am the main process")
    for n in range(4):
        process = multiprocessing.Process(target=whoami,
                                          args=("I am a function %s" % n,))
        process.start()
