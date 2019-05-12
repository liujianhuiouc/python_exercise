# !/usr/bin/env python
# -*- coding: utf-8 -*-

import threading



def lock_test():
    '''
    测试lock是否支持重入，结论:不支持重入
    :return:
    '''
    lock = threading.Lock()
    lock.acquire()
    print("acquire lock")

    lock.acquire()
    print('acquire lock again')

if __name__ == '__main__':
    lock_test()