import os
import time
import multiprocessing


def pinger():
    pinger = os.popen('ping www.bbc.co.uk')
    print list(pinger)


if __name__ == '__main__':
    processes = []

    for _ in range(4):
        p = multiprocessing.Process(target=pinger)
        processes.append(p)

    start = time.clock()

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end = time.clock()

    print('\nserial time', end - start)
