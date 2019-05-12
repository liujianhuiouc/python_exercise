#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import multiprocessing
import subprocess


def test_fork():
    print('start!!!!')
    pid = os.fork()
    # 此后的代码父进程、子进程都会执行
    if pid == 0:
        print('i am a child process %s, parent process id is %s' % (os.getpid(), os.getppid()))
    else:
        print("i am parent processor %s , i created child process is %s" % (os.getpid(), pid))

    print('finish!!!!')


def test_multiprocess():
    """
    测试python扩平台的多进程使用例子
    :return:
    """
    def func(name):
        print('current process id is %s, parent processor id is %s' %
              (os.getpid(), os.getppid()))
        print('name: ', name)

    print('start !!!!')
    processor = multiprocessing.Process(target=func, args=('liujianhui', ))
    # 进程未启动不会生成进程ID
    print("child processor id is %s" % processor.pid)
    processor.start()

    # 进程启动，返回子进程的ID
    print("child processor id is %s" % processor.pid)
    print('current process id is %s' % os.getpid())
    processor.join()
    print('finish !!!!')


def test_subprocess():
    """
    子进程测试，直接执行命令行的方式
    :return:
    """
    cmd = "nslook www.baidu.com"
    subprocess.call(['nslookup', 'wwww.baidu.com'])


if __name__ == '__main__':
    test_subprocess()