#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import time
import traceback
sys.path.insert(0, '/Users/liujianhui/code/internal/pyutil')




class Teacher(object):

    def __init__(self, name, **kwargs):
        self.name = name





class TeacherHigh(Teacher):

    class Meta:
        db_name = '1234'

    def abbreviation(self):
        return self.name



if __name__ == '__main__':
    print('start')
    traceback.format_exc()
    teacher_hign = TeacherHigh(name='liujiahui', score=100)
    print(dir(TeacherHigh))
    print(TeacherHigh.Meta.db_name)
    print(teacher_hign.Meta.db_name)

    params = {"name": "liujianhui", 'teacher': "liuzunhua"}
    params.update({"name": "update", "score": 4})
    print(params)

    print(sys.path)
    from pyutil.program import timing
    timer = timing.Timer()
    dict1 = dict();
    dict1['key'] = 'value'


    timer.timing('hello')
    print(timer.total_seconds())
    print(dict1)

    now = datetime.datetime.now() - datetime.timedelta(days=1)
    print(now)
    print(datetime.datetime.now())
    last = 30
    start_ts = time.mktime((now - datetime.timedelta(days=last - 1)).date().timetuple())
    end_ts = time.mktime(now.date().timetuple())
    print(start_ts)
    print(end_ts)