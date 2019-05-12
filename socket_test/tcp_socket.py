# !/usr/bin/env python
# -*- coding: utf-8 -*-


from socket import socket, AF_INET, AF_UNIX, SOCK_STREAM
import threading
from functools import partial

class LazyConnection(object):
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.type = type
        self.family = family
        self.address = address
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already Connected')

        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock

if __name__ == '__main__':
    '''
    with LazyConnection(('127.0.0.1', 9011)) as socket:
        socket.send('hello world')
        resp = b''.join(iter(partial(socket.recv, 8192), b''))
        print(resp)
    '''

    with LazyConnection('/Users/liujianhui/a1.sock', family=AF_UNIX) as socket:
        socket.send('hello world')
        print('recieved', socket.recv(1024))
        print('end')
