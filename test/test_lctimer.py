# coding:utf-8
from __future__ import unicode_literals
from __future__ import division
from __future__ import print_function
from lctimer import timer


@timer.record
def foo():
    a = 0
    for _ in range(1000000):
        a += 1


# @timer.record
class A:
    def hoo(self):
        c = 0
        for _ in range(1000000):
            c += 1


@timer.record
class B:

    def __init__(self):
        self.words = 'testing'

    @staticmethod
    def ioo():
        c = 0
        for _ in range(1000000):
            c += 1

    c = 0


if __name__ == '__main__':
    aa = timer.record(A)()
    for _ in range(5):
        foo()
        B.ioo()
        aa.hoo()

    timer.sum_up(keep_num=5)
