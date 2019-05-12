# !/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import Queue

class ActorExit(Exception):
    pass

class Result(object):
    def __init__(self):
        self._semaphore = threading.Event()

    def get(self):
        self._semaphore.wait()
        if isinstance(self._result, Exception):
            raise self._result
        return self._result

    def set(self, result):
        self._result = result
        self._semaphore.set()

class Actor(object):
    def __init__(self, processor):
        self._mailbox = Queue.Queue()
        self._processor = processor

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def start(self):
        self._event = threading.Event()
        thread = threading.Thread(target=self._bootstrap)
        thread.start()

    def close(self):
        self.send(ActorExit)

    def join(self):
        self._event.wait()

    def process(self, msg):
        return self._processor(msg)

    def _run(self):
        while 1:
            msg = self.recv()
            self.process(msg)

    def _bootstrap(self):
        try:
            self._run()
        except ActorExit:
            pass
        finally:
            self._event.set()



class Worker(Actor):
    def submit(self, msg):
        result = Result()
        self.send((msg, result))
        return result

    def process(self, msg_result):
        msg, result = msg_result
        try:
            process_result = super(Worker, self).process(msg)
        except Exception as e:
            result.set(e)
        finally:
            result.set(process_result)

def test_actor():
    def print1(msg):
        print(msg)

    actor = Actor(print1)
    actor.start()
    actor.send("hello world")
    actor.send("hello world")

    actor.close()

def test_worker():
    def process(msg):
        print(msg)
        return 'hello ' + msg
    worker = Worker(process)

    worker.start()
    result = worker.submit("liujianhui")
    print(result.get())
    worker.close()

if __name__ == '__main__':
    test_worker()




