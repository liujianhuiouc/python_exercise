# !/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

class Student(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.age = kwargs.get('age', 0)

    def info(self):
        print('name=%s, age=%s' % (self.name, self.age))

def countdown(event):
    event.set()
    print('countdown')



if __name__ == '__main__':
    liujianhui = Student(name='liujianhui', age=10)
    myThread = threading.Thread(name='test', target=liujianhui.info)
    myThread.start()
    print(myThread.daemon)
    myThread.join()

    event = threading.Event()
    myThread = threading.Thread(target=countdown, args=(event, ))
    myThread.start()
    time.sleep(5)
    print('timeout')
    event.wait()
    print("finish")