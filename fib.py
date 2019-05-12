#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Fib(object):

    def __init__(self, value):
        self.value = value
        self.pos = 0
        self.a = 0
        self.b = 0


    def __str__(self):
        return "fib: %s".format(self.value)


    def __iter__(self):
        return self


    def __next__(self):
        if self.pos > self.value:
            raise StopIteration

        if not self.a:
            self.a = 1
            next_value = 1

        if not self.b:
            self.b = 1
            next_value = 1

        self.pos += 1
        next_value = self.a + self.b
        self.a = self.b
        self.b = next_value

        return next_value

    next = __next__




if __name__ == '__main__':
    fib = Fib(10)
    for i in Fib(10):
        print(i)