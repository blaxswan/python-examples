import threading
from timeit import default_timer as timer


def fib(number):
    if number <= 1: return 1
    return fib(number - 2) + fib(number - 1)


threads = []
for _ in range(5):
    t = threading.Thread(target=fib, args=(30,))
    threads.append(t)

start = timer()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = timer()

print('\nthreads time', end - start)
