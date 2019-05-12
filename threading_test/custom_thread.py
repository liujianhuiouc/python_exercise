# !/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

class CustomThread(threading.Thread):
    def run(self):
        try:
            super(CustomThread, self).run()
        except Exception as e:
            self._exception = e
        finally:
            pass

    def join(self, timeout=None):
        super(CustomThread, self).join(timeout)
        if hasattr(self, '_exception'):
            raise self._exception



if __name__ == '__main__':
    def print1():
        print("hello")
        time.sleep(10)
        #raise RuntimeError('test')

    thread = CustomThread(target=print1)
    thread.start()
    thread.join()