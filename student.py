#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import test
class StudentMetaclass(type):

    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        return type.__new__(cls, *args, **kwargs)

class Student(object):
    """
    学生类
    """

    # __slots__ = ('name', 'age', 'score', '__teacher')

    def __init__(self, name, score, **kwargs):
        self.name = name
        self.score = score
        self.__teacher = 'hello'
        self.kwargs = kwargs
        print("student")

    def to_string(self):
        return 'name: ' + self.name

    def to_string(self, *args, **kwargs):
        return "aaa"




class Employee:


    def __init__(self, name, score):
        print("employee")
        self.name = name

    def to_string(self):
        return "employee" + self.name

class StudentHigh(Employee, Student):

    school = "1234564"
    print(school)

    def __init__(self, name, score):
        # super(StudentHigh, self).__init__(name, score)
        Employee.__init__(self, name, score)
        Student.__init__(self, name, score)
        self.name = "high"


if __name__ == '__main__':
    '''
    Student.xxx = lambda x : print(x)

    student = Student('liujianhui', 100)
    student.xxx()


    a = student.xxx
    a()
    test.Data = Student
    student = test.Data('hello', 2)
    student.xxx()
    '''

    student = Student('1', 1)
    print(student.to_string.__name__)
    print(student.to_string('liujianhui'))
    print(student.to_string())
    try:
        1 /0
    except ZeroDivisionError as e:
        print(e)
    finally:
        print('finally')

    logging.error('hello %s, %s', 'liujianhui', 'hi')