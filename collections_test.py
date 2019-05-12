# !/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import namedtuple

def test_namedtuple():
    result = namedtuple('name', 'age')
    result(('liujianhui', '30'))
    print(result)

if __name__ == '__main__':
    test_namedtuple()