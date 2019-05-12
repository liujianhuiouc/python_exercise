# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
import dis
import socket
import sys


DEFAULT_SOCKET_PATH = '/opt/tmp/sock/databus_collector.seqpacket.sock'
DEFAULT_STREAM_SOCKET_PATH = '/Users/liujianhui/eclipse/cpp-2019-03/a.sock'


def init_sock():
    sock_stream = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock_stream.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)
    sock_stream.settimeout(1000)
    sock_stream.connect(DEFAULT_STREAM_SOCKET_PATH)
    sock_stream.settimeout(1000)

if __name__ == '__main__':
    def countdown(coundown):
        while 1 > 0:
            coundown -= 1
            print('countdown')
            # sock_stream.recv(8192)
            time.sleep(10000)

    def print1(a):
        print(a)

    start_time = time.time()
    cw = 10000000
    countdown(cw)
    print(time.time() - start_time)

    dis.dis(countdown)
    # sys.setcheckinterval(10)


    thread1 = threading.Thread(target=countdown, args=(cw / 2,))
    thread2 = threading.Thread(target=countdown, args=(cw / 2,))
    start_time = time.time()
    thread1.start()
    thread2.start()

    threading.Thread(target=print1, args=(cw / 2,)).start()
    print('start ok')

    # thread1.join()
    # thread2.join()
    print(time.time() - start_time)

