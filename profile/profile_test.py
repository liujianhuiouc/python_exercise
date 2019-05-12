# !/usr/bin/env python
# -*- coding:utf-8 -*-



def test():
    test1()

def test1():
    pass


if __name__ == '__main__':
    import cProfile

    cProfile.run("test()")