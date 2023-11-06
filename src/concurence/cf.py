from concurrent import futures
import math
import time
import sys


def calc(val):
    time.sleep(1)
    return math.sqrt(val)


def use_threads(num, values):
    t1 = time.time()
    with futures.ThreadPoolExecutor(num) as tex:
        tex.map(calc, values)
    t2 = time.time()
    return t2 - t1


def use_processes(num, values):
    t1 = time.time()
    with futures.ProcessPoolExecutor(num) as tex:
        tex.map(calc, values)
    t2 = time.time()
    return t2 - t1


def main(workers, values):
    print(f"Using {workers} workers for {len(values)} values")
    print(f"Threads took {use_threads(workers, values):.4f}")
    print(f"Processes took {use_processes(workers, values):.4f}")


if __name__ == "__main__":
    workers = int(sys.argv[1])
    values = [num for num in range(1, 6)]
    main(workers, values)
