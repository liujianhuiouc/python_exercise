import Queue
import socket
import os

import select
import threading


class PollableQueue(object):

    def __init__(self, *args, **kwargs):
        #super(PollableQueue, self).__init__(*args, **kwargs)
        self._queue = Queue.Queue()
        print("os name", os.name)
        # Create a pair of connected sockets
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            # Compatibility on non-POSIX systems
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

    def fileno(self):
        return self._getsocket.fileno()

    def put(self, item):
        self._queue.put(item)
        self._putsocket.send(b'x')

    def get(self):
        self._getsocket.recv(1)
        return self._queue.get()


def consumer(queues):
    '''
    Consumer that reads data on multiple queues simultaneously
    '''
    while True:
        try:
            can_read, _, _ = select.select(queues,[],[])
            for r in can_read:
                item = r.get()
                print('Got:', item)
        except Exception as e:
            print('error', e)


if __name__ == '__main__':
    q1 = PollableQueue()
    q2 = PollableQueue()
    q3 = PollableQueue()
    t = threading.Thread(target=consumer, args=([q1,q2,q3],))
    t.daemon = False
    t.start()

    # Feed data to the queues
    q1.put(1)
    q2.put(10)
    q3.put('hello')
    q2.put(15)