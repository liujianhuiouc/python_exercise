# !/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from threading_test import local


class MyThread(threading.Thread):
    def __init__(self, **kwargs):
        self.request_id = getattr(local, 'request_id', 'none')
        print(self.request_id)
        super(MyThread, self).__init__()

    def run(self):
        setattr(local, 'request_id', self.request_id)
        print(getattr(local, 'request_id'))


def test_local():
    local = threading.local()
    local.xxx = 'liujianhui'
    aa = local.xxx


    def test_local():
        local = threading.local()
        local.requestid = aa
        print(getattr(local, "requestid", None))

    thread = threading.Thread(target=test_local())
    thread.start()


if __name__ == '__main__':
    setattr(local, 'request_id', 'liujiannhui')
    print(local)
    print(threading.local())
    print(threading.local())
    local1 = threading.local()
    print(local1)
    print(threading.local() is threading.local())
    print(getattr(local, 'request_id'))
    thread = MyThread()
    thread.start()


