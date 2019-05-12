#!/usr/bin/env python
# -*- coding: utf-8 -*-


from enum import Enum


class Status(Enum):
    SUCCESS = 1
    TIMEOUT = 2


if __name__ == '__main__':

    for key, value in Status.__members__.items():
        print(key, value.value)

    print(Status(1))
