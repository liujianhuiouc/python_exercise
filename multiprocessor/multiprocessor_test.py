

import multiprocessing
import time
import os
from multiprocessing import Queue

class Actor(object):
    def __init__(self):
        self._queue = Queue()

    def dispatch(self):
        while 1:
            try:
                print('pid %s ' % os.getpid())
                msg = self._queue.get()
                print(msg)
            except Exception:
                pass

    def send(self, msg):
        self._queue.put(msg)


if __name__ == '__main__':
    actor = Actor()

    for i in range(2):
        processor = multiprocessing.Process(target=actor.dispatch)
        processor.start()
        print('processor start, id is %s' % processor.pid)

    i = 0
    while 1:
        actor.send(i)
        i += 1
        time.sleep(1)