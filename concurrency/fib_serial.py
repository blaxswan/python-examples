import time
from timeit import default_timer as Timer


def fib(number):
    if number <= 1: return 1
    return fib(number - 2) + fib(number - 1)


start = time.clock()

for _ in xrange(4):
    fib(30)

end = time.clock()

print('\nserial time', end - start)
