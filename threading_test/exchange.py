# !/usr/bin/env python
# -*- coding: utf-8 -*-


from collections import defaultdict

class Exchange(object):
    def __init__(self):
        self._subscribers = set()

    def attach(self, subscriber):
        self._subscribers.add(subscriber)

    def detach(self, subscriber):
        self._subscribers

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


class Data(object):
    def __init__(self, id):
        self._id = id

    def __eq__(self, other):
        return self._id == other._id

    def __repr__(self):
        return "id %s" % self._id

    def __hash__(self):
        return self._id

_exchange = defaultdict(Exchange)

def get_exchange(name):
    return _exchange[name]

class PrintSubscriber(object):
    def send(self, msg):
        print('msg %s' % msg)

if __name__ == '__main__':
    exchange = get_exchange("liujianhui")
    exchange.attach(PrintSubscriber())
    exchange.send('hello liujianhui')