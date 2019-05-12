# !/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('pre start')
        print(args)
        print(kwargs)
        return func(*args, **kwargs)

    return wrapper


def async1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('pre start')
        print(args)
        print(kwargs)
        func(*args, **kwargs)
        return None

    return wrapper

def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('text is %s' % text)
            return func(*args, **kwargs)

        return wrapper

    return decorator

def preInit(cls):
    @functools.wraps(cls)
    def xxx(*args, **kwargs):
        cls(*args, **kwargs)
        return cls

    return xxx

@preInit
class Student(object):
    def __init__(self, **kwargs):
        pass

@async1
def test():
    print("test")
    return "finish"





if __name__ == '__main__':

    print(Student)
    print(Student())
    print(test())