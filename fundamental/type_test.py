#!/urs/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    def func(self, name):
        print('name: ', name)

    Hello = type('Hello', (object, ), dict(hello=func))
    hello = Hello()
    hello.hello('liujianhui')