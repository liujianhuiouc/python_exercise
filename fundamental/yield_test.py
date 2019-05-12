# !/usr/bin/env python
# -*- coding:utf-8 -*-

import contextlib
import threading

@contextlib.contextmanager
def get_generator(num):
    i = 0
    try:
        while i < num:
            try:
                yield i
                i += 1
            finally:
                print('finaly %s' % i)
    finally:
        print("outer %s" % i)


def test_generator():
    with get_generator(1) as a:
        print('a %s ' % a)

    print('ok')


def _generator():
    try:
        while 1:
            x = yield print1('yield')
            print(x)
    finally:
        print('finally')

def print1(msg):
    print(msg)

def outer_gen():
    print(_generator())
    print('outer_gen')


def generator():
    print("start")
    while 1:
        m = yield
        print("msg", m)


def test_generator1():
    gen = generator()
    # print(next(gen))
    print(gen.send(None))
    print(gen.send('liujianhui'))


def generator_wait():
    try:
        event = threading.Event()
        print('start generator_wait')
        yield

        print('finish generator_wait')
    finally:
        print('finally generator_wait')
        event.wait()


def gen():
    try:
        print('gen')
        yield
    finally:
        print('finally gen')

def test_multi_thread():
    a = generator_wait()
    def next_a():
        print('next_a')
        next(a)
    #next_a()
    threading.Thread(target=next_a).start()
    #threading.Thread(target=next_a).start()

def test_yield_finnally():
    generator = _generator()
    next(generator)
    generator.send('liujianhui')

if __name__ == '__main__':
    #a = _generator()
    #next(a)






    def gen1():
        try:
            print('gen')
            yield
        finally:
            print('finally gen1')

    a = gen1()
    next(a)

    del a
    event = threading.Event()
    event.wait()
