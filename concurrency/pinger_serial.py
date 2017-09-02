import os
import time


def pinger():
    pinger = os.popen('ping www.bbc.co.uk', 'r')
    print list(pinger)


start = time.clock()

for _ in xrange(4):
    pinger()

end = time.clock()

print('\nserial time', end - start)
