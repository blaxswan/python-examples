import os
import threading
from timeit import default_timer as timer


def pinger():
    pinger = os.popen('ping www.bbc.co.uk')
    print list(pinger)


threads = []
for _ in range(4):
    t = threading.Thread(target=pinger)
    threads.append(t)

start = timer()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = timer()

print('\nthreads time', end - start)
