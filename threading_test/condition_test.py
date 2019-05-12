# !/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

class PeriodicTimer(object):
    def __init__(self, interval):
        self.interval = interval
        self.flag = 0
        self._cv = threading.Condition()

    def start(self):
        thread = threading.Thread(name='tick', target=self.run)
        thread.start()

    def run(self):
        while 1:
            with self._cv:
                self.flag ^= 1
                self._cv.notify_all()

            time.sleep(self.interval)

    def wait_for_tick(self):
        with self._cv:
            last_flag = self.flag
            while last_flag == self.flag:
                self._cv.wait()


if __name__ == '__main__':
    periodic_timer = PeriodicTimer(interval=2)
    periodic_timer.start()
    def countdown():
        while 1:
            periodic_timer.wait_for_tick()
            print('countdown')

    def countup():
        while 1:
            periodic_timer.wait_for_tick()
            print('countup')

    threading.Thread(target=countdown()).start()
    threading.Thread(target=countup()).start()