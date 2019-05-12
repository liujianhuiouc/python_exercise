#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import time



def action(content):
    print(content)
    time.sleep(100000)


def test_direct_thread():
    for i in range(4):
        thread = threading.Thread(target=action, args=('liujianhui', ))
        thread.setDaemon(True)
        thread.start()

    print("hello main threading_test")
    print('threading_test count %s' % threading.active_count())



class Mythread(threading.Thread):

    def __init__(self, content):
        super(Mythread, self).__init__()
        self.content = content


    def run(self):
        print('MyThread is %s' % self.content)
        time.sleep(10)


def test_inherit_thread():
    thread = Mythread('liujianhui')
    thread.start()

    print("main threading_test over")
    print(threading.enumerate())
    print(threading.current_thread())


lock = threading.RLock()

def test_lock():
    lock.acquire()
    lock.acquire()

    print("test_lock")

    lock.release()
    lock.release()

if __name__ == '__main__':
    test_lock()


