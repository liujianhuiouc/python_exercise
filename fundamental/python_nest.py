# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Example(object):
    def __init__(self, appid):
        self.map = dict()
        self[appid] = appid
        self.appid = appid
        self.name = 'liujianhui'
        super(Example, self).__init__()

    def __setitem__(self, key, value):
        print('__setitem__ (%s, %s)' % (key, value))
        self.name = '123'
        self.map[key] = value


if __name__ == '__main__':
    example = Example(1234);
