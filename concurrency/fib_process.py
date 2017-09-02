import time
import multiprocessing
from multiprocessing import Process


def fib(number):
    if number <= 1: return 1
    return fib(number - 2) + fib(number - 1)


if __name__ == '__main__':
    processes = []

    for _ in range(5):
        p = Process(target=fib, args=(30,))
        processes.append(p)

    start = time.clock()

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end = time.clock()

    print('\nprocesses time', end - start)
    print('cores', multiprocessing.cpu_count())
