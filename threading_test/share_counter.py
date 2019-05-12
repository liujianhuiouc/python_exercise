# !/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

class ShareCounter(object):
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()


    def incr(self, delta=1):
        with self._lock:
            self._value += delta


    def decr(self, delta=1):
        with self._lock:
            self._value -= delta


    def value(self):
        return self._value