"""
This is my first python program
"""

import sys

import pprint
import time
import student

print("import test.py")
print(__file__)


class Data(object):
    pass

def test1():
    print("hello")
    print(__file__)

def test():
    pass

a = Data()
print(a)


if __name__ == "__main__":

    print(time.time())
    import types
    def gen():
        yield


    print(isinstance(gen(), types.GeneratorType))
    print(isinstance(gen, types.GeneratorType))
    print(gen)

    def hello():
        pass

    print(hello())
    result = list()
    map(lambda x: result.append(x[0]), list())

    results = []
    results.append({"a":"a", "b":"b"})
    for result in results:
        print(result)

    class EventParam(dict):
        def __init__(self, app_id):
            self.app_id = app_id
            self.container = dict()

        def __getitem__(self, item):
            print('__getitem__')
            if item in self.container:
                return self.container[item]

            event_param = {}
            self.container[item] = event_param
            return event_param

        def __setitem__(self, key, value):
            print('__setitem__')
            self.container[key] = value

        def __contains__(self, key):
            print('__contain__')
            return key in self.container

        def get(self, key):
            return self.container[key]


    #a = EventParam(['1', '2', '4'])
    a = EventParam(1)
    # a['aa'] = 'aa'

    if 'a' not in a:
        pass
    # student_high = student.StudentHigh('liujianhui', 100)
    # print(student_high.to_string())
    #
    # pprint.pprint(student.StudentHigh.mro())
    #
    # student_high.to_string()


    # student1 = student.Student('liujianhui', 100)
    # print(student1.to_string())
    # print(student1._Student__teacher)
    #
    # student_high = student.StudentHigh('liujianhui', 20)
    # print(student_high.name)
    # print(type(student_high))
    # print(student_high.school)
    # print('to_string is %s' % student_high.to_string())
    #
    # print(dir(student.Student))
    # print(student1.__class__)
    # student.Student.address = 'zhangjiajie'
    # print(student1.address)
    # student.Student.address = 'nanjing'
    # print(student1.address)
    # print(student.Student('nihao', 200).address)
    #
    # print(student1.address)


